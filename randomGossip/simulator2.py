#! /usr/bin/python

import commands

def simula(nodes):
	MAXRIC=0
	inviati = []
	ricevuti = []
	scarti = []

	for j in range(0,4):
		inviati += [0]
		ricevuti += [0]
		scarti += [0]

	for i in range(0,4):

		print("i:"+str(i)+"\n")

		f = open("VarianteK.h", "w")
		
        	stringa = '#define MAXRIC '+str(MAXRIC)+"\n" 
        	f.write(stringa)
		stringa2 = '#define NODES '+str(nodes)
		f.write(stringa2)
        	f.close()
        	
		if MAXRIC==0: print("Compilazione con Flooding puro\n")
		else: print("Compilazione con K="+str(MAXRIC)+"\n")

        	commands.getoutput("make micaz sim")
        	print("[OK]")

        	print("Esecuzione test.py...")
        
        	commands.getoutput("./test.py")

        	ris = open("Inoltri.txt", "r")
        	ris_lines = ris.readlines()
        	numero= len(ris_lines)
        	ris.close()
		
	        print("[OK] - Pacchetti Inviati: "+str(numero)+"\n")
		
	

	 	ris2 = open("Ricevuti.txt", "r")
	        ris_lines2 = ris2.readlines()
	        numero2= len(ris_lines2)
	        ris2.close()
		
	        print("[OK] - Pacchetti Ricevuti: "+str(numero2)+"\n")
		


	 	ris3 = open("Scarti.txt", "r")
	        ris_lines3 = ris3.readlines()
	        numero3= len(ris_lines3)
	        ris3.close()
		
	        print("[OK] - Pacchetti Scartati: "+str(numero3)+"\n")

		inviati[i] += numero
		ricevuti[i] += numero2
		scarti[i] += numero3

		print(inviati)

		if MAXRIC==0: MAXRIC = 4
		else: MAXRIC = MAXRIC*2

	
    
#risultati = []
print '*** SIMULAZIONE CON VARIAZIONE DI NUMERO DI NODI, K FISSATO ***'
print '*** Topologia con 50 nodi...'

t = open("topo_param.txt", "w")
t.write('50\n')
t.close()
commands.getoutput("./generatoreTopo.py")
simula(50)
print '*** OK ***\n'

print '*** Topologia con 100 nodi...'
t = open("topo_param.txt", "w")
t.write('100\n')
t.close()
commands.getoutput("./generatoreTopo.py")
simula(100)
print '*** OK ***\n'

print '*** Topologia con 150 nodi...'
t = open("topo_param.txt", "w")
t.write('150\n')
t.close()
commands.getoutput("./generatoreTopo.py")
simula(150)
print '*** OK ***\n'

print '*** Topologia con 200 nodi...'
t = open("topo_param.txt", "w")
t.write('200\n')
t.close()
commands.getoutput("./generatoreTopo.py")
simula(200)
print '*** OK ***\n'


for i in risultati:
    for j in i:
        ris1.write(str(j)+' ')
    ris1.write('\n')
ris1.close()

print("SIMULAZIONE TERMINATA...\n")


