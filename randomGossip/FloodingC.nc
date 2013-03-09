
#include "Timer.h"
#include "Flooding.h"
 
#define PROBABILITY 50

module FloodingC {
  uses {
    interface Boot;
    interface Receive;
    interface AMSend;
    interface Timer<TMilli> as MilliTimer;
    interface SplitControl as AMControl;
    interface Packet;
    interface Random;
    interface ParameterInit<uint16_t> as Seed;
  }
}
implementation {

  nx_uint16_t nodes[NODES];
  nx_uint16_t nodes2[NODES];
 
  message_t packet;

  uint16_t message = 0;
	
  uint16_t cont = 0;

  uint16_t i;

  float r;

  event void Boot.booted() {
    //float r;
      
    dbg("Boot", "Node %hhu booted\n", TOS_NODE_ID);
    call AMControl.start();
    for (i=0; i<NODES; ++i) {
        nodes[i] = 0;
    }
    //r = (float) call Random.rand16() / 65536;
    
    
  }

  // C'è un tempo da attendere prima che la radio
  // finisca di avviarsi. Quando ha finito di attivarsi
  // viene generato l'evento startDone. Qui parte
  // l'applicazione vera e propria
  event void AMControl.startDone(error_t err) {
    if (err == SUCCESS) {
	if (TOS_NODE_ID == SOURCE_NODE) call MilliTimer.startOneShot(500); // all'incirca (tinyos usa la base 2) 1 sec = 1024 msec
    }
    else {
      call AMControl.start(); // proviamo a farla ripartire
    }
  }

  event void AMControl.stopDone(error_t err) {
    // do nothing
  }
  
  event void MilliTimer.fired() {
	//scaduto il timer creo la locazione del pkt da inviare e incremento il payload del messaggio
      radio_count_msg_t* rcm = (radio_count_msg_t*)call Packet.getPayload(&packet, (int) NULL);
      //message++;
	
	//incremento il num di sequenza nel vettore nodes[mia_posizione] 
      nodes[TOS_NODE_ID]++;

	
      if (call Packet.maxPayloadLength() < sizeof(radio_count_msg_t)) {
        dbg("GossipBCastC", "size problem\n");
	return;
      }

      //creo il pacchetto da inviare
      rcm->message = message;
      rcm->id = TOS_NODE_ID;
      rcm->seq = nodes[TOS_NODE_ID];


	if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
		dbg("Inoltro", "Pacchetto inviato id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);
		//locked = TRUE; // blocco la radio, se uno tenta di inviare tanti pacchetti velocemente.
	}
    }
  

  event message_t* Receive.receive(message_t* bufPtr, void* payload, uint8_t len) {
	/*sta roba non serve è per l'inoltro probabilistico    
	
        //call Seed.init((int) bufPtr * (int) payload);  // Seed iniziale pseudo-random
        dbg("GossipBCastC", "Received packet of length %hhu.\n", len);
	*/    
	
	if (len != sizeof(radio_count_msg_t)) {return bufPtr;} // se la dim non è 16byte ignoriamo il pacchetto
	else {
        // Punto al payload del pacchetto ricevuto
        radio_count_msg_t* rcm = (radio_count_msg_t*)payload;
        // Punto al payload del nuovo pacchetto
        radio_count_msg_t* rcm2 = (radio_count_msg_t*)call Packet.getPayload(&packet, (int) NULL); 

        //if (rcm->seq > nodes[rcm->id] && rcm->id != TOS_NODE_ID) {
        //if (rcm->seq > nodes[rcm->id]) {
       	dbg("Ricevuti", "Ricevuto Pacchetto id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);
	if(MAXRIC!=0){
	       	if(nodes[rcm->id]==rcm->seq){
			++nodes2[rcm->id];
			if(nodes2[rcm->id] < MAXRIC){
			 	rcm2->id = rcm->id;
			 	rcm2->seq = rcm->seq;
	 			rcm2->message = rcm->message;
		 		if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
		 	  		dbg("Inoltro", "Pacchetto inoltrato id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);	
		 	  		//locked = TRUE; // blocco la radio, se uno tenta di inviare tanti pacchetti velocemente.
		 		}
			}
			else dbg("Scarti", "Pacchetto scartato id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);
		}
		else if(nodes[rcm->id]>rcm->seq) dbg("Scarti", "Pacchetto scartato id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);
		else {
			nodes[rcm->id] = rcm->seq;  // Aggiorno il numero di sequenza
			nodes2[rcm->id] = 0;

			rcm2->id = rcm->id;
			rcm2->seq = rcm->seq;
	 		rcm2->message = rcm->message;
		 	if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
		 		dbg("Inoltro", "Pacchetto inoltrato id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);	
		 		//locked = TRUE; // blocco la radio, se uno tenta di inviare tanti pacchetti velocemente.
		 	}
		}
	}
	else{
		nodes[rcm->id] = rcm->seq;  // Aggiorno il numero di sequenza
		nodes2[rcm->id] = 0;
		rcm2->id = rcm->id;
		rcm2->seq = rcm->seq;
	 	rcm2->message = rcm->message;
		if (call AMSend.send(AM_BROADCAST_ADDR, &packet, sizeof(radio_count_msg_t)) == SUCCESS) {
			dbg("Inoltro", "Pacchetto inoltrato id=%hhu seq=%hhu message=%hhu\n", rcm->id, rcm->seq, rcm->message);	
			//locked = TRUE; // blocco la radio, se uno tenta di inviare tanti pacchetti velocemente.
		}
	}

	//Invio di un nuovo pkt probabilistico
	r = (float) call Random.rand16() / 65536;
	if(r < (float)PROBABILITY/100) call MilliTimer.startOneShot(r*10000);
	
        return bufPtr;
    }
  }

  event void AMSend.sendDone(message_t* bufPtr, error_t error) {
	
    if (&packet == bufPtr) {  // controlliamo che è esattamente il pacchetto che stavamo trasmettendo
      //locked = FALSE; // sblocco la radio
    }
	
 	
  }

}
