#! /usr/bin/python

import commands
import os

def simula(nodes):
		
		f = open("VarianteK.h", "w")
		
		stringa2 = '#define NODES '+str(nodes)
		f.write(stringa2)
        	f.close()

        	commands.getoutput("make micaz sim")
        	print("[OK]")

        	print("Esecuzione test.py...")
        
        	commands.getoutput("./test.py")

        	ris = open("Inoltri.txt", "r")
        	ris_lines = ris.readlines()
        	numero= len(ris_lines)
        	ris.close()
		
	        print("[OK] - Pacchetti Inviati: "+str(numero)+"\n")
		
		if nodes!=200:
			 risultFPi.write(str(numero)+" ")
			

		else: 
			risultFPi.write(str(numero)+"\n")
			

	 	ris2 = open("Ricevuti.txt", "r")
	        ris_lines2 = ris2.readlines()
	        numero2= len(ris_lines2)
	        ris2.close()
		
	        print("[OK] - Pacchetti Ricevuti: "+str(numero2)+"\n")
		
		if nodes!=200:
			risultFPr.write(str(numero2)+" ")
			
		else: 
			risultFPr.write(str(numero2)+"\n")
			

	 	ris3 = open("Scarti.txt", "r")
	        ris_lines3 = ris3.readlines()
	        numero3= len(ris_lines3)
	        ris3.close()
		
	        print("[OK] - Pacchetti Scartati: "+str(numero3)+"\n")

		if nodes!=200:
			risultFPs.write(str(numero3)+" ")
			

		else: 
			risultFPs.write(str(numero3)+"\n")
			

		

print '*** SIMULAZIONE CON VARIAZIONE DI NUMERO DI NODI, FLOODING PURO ***'
print '*** Topologia con 50 nodi...'
risultFPi = open("risultatiFPi.txt","w")
risultFPr = open("risultatiFPr.txt","w")
risultFPs = open("risultatiFPs.txt","w")
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
simula(100)
print '*** OK ***\n'

print '*** Topologia con 150 nodi...'
t = open("topo_param.txt", "w")
t.write('150\n')
t.close()
simula(150)
print '*** OK ***\n'

print '*** Topologia con 200 nodi...'
t = open("topo_param.txt", "w")
t.write('200\n')
t.close()
simula(200)
print '*** OK ***\n'
risultFP = open("risultatiFP.txt","w")
risultFPi = open("risultatiFPi.txt","r")
risultFPr = open("risultatiFPr.txt","r")
risultFPs = open("risultatiFPs.txt","r")

lines = risultFPi.readlines()
risultFP.writelines(lines)
lines = risultFPr.readlines()
risultFP.writelines(lines)
lines = risultFPs.readlines()
risultFP.writelines(lines)



risultFP.close();


os.remove("risultatiFPi.txt")
os.remove("risultatiFPr.txt")
os.remove("risultatiFPs.txt")

print("SIMULAZIONE TERMINATA...\n")
