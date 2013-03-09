#! /usr/bin/python

import commands
import os

def simula(nodes):
	MAXRIC=4

	for i in range(0,3):
		f = open("VarianteK.h", "w")
		
        	stringa = '#define MAXRIC '+str(MAXRIC)+"\n" 
        	f.write(stringa)
		stringa2 = '#define NODES '+str(nodes)
		f.write(stringa2)
        	f.close()
        	
		print("Compilazione con K="+str(MAXRIC)+"\n")

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
			if MAXRIC==4: risultK4i.write(str(numero)+" ")
			elif MAXRIC==8: risultK8i.write(str(numero)+" ")
			else: risultK16i.write(str(numero)+" ")

		else: 
			if MAXRIC==4: risultK4i.write(str(numero)+"\n")
			elif MAXRIC==8: risultK8i.write(str(numero)+"\n")
			else: risultK16i.write(str(numero)+"\n")

	 	ris2 = open("Ricevuti.txt", "r")
	        ris_lines2 = ris2.readlines()
	        numero2= len(ris_lines2)
	        ris2.close()
		
	        print("[OK] - Pacchetti Ricevuti: "+str(numero2)+"\n")
		
		if nodes!=200:
			if MAXRIC==4: risultK4r.write(str(numero2)+" ")
			elif MAXRIC==8: risultK8r.write(str(numero2)+" ")
			else: risultK16r.write(str(numero2)+" ")

		else: 
			if MAXRIC==4: risultK4r.write(str(numero2)+"\n")
			elif MAXRIC==8: risultK8r.write(str(numero2)+"\n")
			else: risultK16r.write(str(numero2)+"\n")

	 	ris3 = open("Scarti.txt", "r")
	        ris_lines3 = ris3.readlines()
	        numero3= len(ris_lines3)
	        ris3.close()
		
	        print("[OK] - Pacchetti Scartati: "+str(numero3)+"\n")

		if nodes!=200:
			if MAXRIC==4: risultK4s.write(str(numero3)+" ")
			elif MAXRIC==8: risultK8s.write(str(numero3)+" ")
			else: risultK16s.write(str(numero3)+" ")

		else: 
			if MAXRIC==4: risultK4s.write(str(numero3)+"\n")
			elif MAXRIC==8: risultK8s.write(str(numero3)+"\n")
			else: risultK16s.write(str(numero3)+"\n")

		if MAXRIC==16: MAXRIC = 4
		else: MAXRIC = MAXRIC*2
    

print '*** SIMULAZIONE CON VARIAZIONE DI NUMERO DI NODI, K RICEZIONI VARIABILI ***'
print '*** Topologia con 50 nodi...'

risultK4i = open("risultatiK4i.txt","w")
risultK8i = open("risultatiK8i.txt","w")
risultK16i = open("risultatiK16i.txt","w")

risultK4r = open("risultatiK4r.txt","w")
risultK8r = open("risultatiK8r.txt","w")
risultK16r = open("risultatiK16r.txt","w")

risultK4s = open("risultatiK4s.txt","w")
risultK8s = open("risultatiK8s.txt","w")
risultK16s = open("risultatiK16s.txt","w")
t = open("topo_param.txt", "w")
t.write('50\n')
t.close()

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


risultK4i = open("risultatiK4i.txt","r")
risultK8i = open("risultatiK8i.txt","r")
risultK16i = open("risultatiK16i.txt","r")

risultK4r = open("risultatiK4r.txt","r")
risultK8r = open("risultatiK8r.txt","r")
risultK16r = open("risultatiK16r.txt","r")

risultK4s = open("risultatiK4s.txt","r")
risultK8s = open("risultatiK8s.txt","r")
risultK16s = open("risultatiK16s.txt","r")



risultK4 = open("risultatiK4.txt","w")
lines = risultK4i.readlines()
risultK4.writelines(lines)
lines = risultK4r.readlines()
risultK4.writelines(lines)
lines = risultK4s.readlines()
risultK4.writelines(lines)

risultK4.close();

risultK8 = open("risultatiK8.txt","w")
lines = risultK8i.readlines()
risultK8.writelines(lines)
lines = risultK8r.readlines()
risultK8.writelines(lines)
lines = risultK8s.readlines()
risultK8.writelines(lines)

risultK8.close();

risultK16 = open("risultatiK16.txt","w")
lines = risultK16i.readlines()
risultK16.writelines(lines)
lines = risultK16r.readlines()
risultK16.writelines(lines)
lines = risultK16s.readlines()
risultK16.writelines(lines)

risultK16.close();

os.remove("risultatiK4i.txt")
os.remove("risultatiK8i.txt")
os.remove("risultatiK16i.txt")

os.remove("risultatiK4r.txt")
os.remove("risultatiK8r.txt")
os.remove("risultatiK16r.txt")

os.remove("risultatiK4s.txt")
os.remove("risultatiK8s.txt")
os.remove("risultatiK16s.txt")
print("SIMULAZIONE TERMINATA...\n")
