#include "Flooding.h"

configuration FloodingAppC {}
implementation {
  components MainC, FloodingC as App;
  components new AMSenderC(AM_RADIO_COUNT_MSG);
  components new AMReceiverC(AM_RADIO_COUNT_MSG);
  components new TimerMilliC();
  components ActiveMessageC;
  components RandomC;

  /* Wirings */
  
  App.Boot -> MainC.Boot;
  
  App.Receive -> AMReceiverC;
  App.AMSend -> AMSenderC;
  App.AMControl -> ActiveMessageC;
  App.MilliTimer -> TimerMilliC;
  App.Packet -> AMSenderC;

  /* Wirings for RandomC component */
  /* Al boot TinyOS chiama SoftwareInit.init. Facendo questo collegamento,
   * verrà inoltre chiamato RandomC.init. Questo servirà a settare il seed
   * iniziale del generatore di numeri casuali all'ID del nodo
   */
  MainC.SoftwareInit -> RandomC;
  App.Random -> RandomC;
  
  App.Seed -> RandomC.SeedInit;
 

}


