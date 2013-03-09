#! /usr/bin/python
from TOSSIM import *
import sys

import numpy as np
import math


#inizializzazione tossim
t = Tossim([])   
r = t.radio()

#apro il file che contiene la topologia generata da generatoreTopo
f = open("topo.txt", "r")
f2 = open("topo_param.txt", "r")
lines = f2.readlines()
num_nodi = int(lines[0])

# topologia statica
lines = f.readlines()
for line in lines:
  s = line.split()
  if (len(s) > 0):
    r.add(int(s[0]), int(s[1]), float(s[2]))

#apro i canali per il debug

scarti = open("Scarti.txt", "w")
t.addChannel("Scarti", scarti)

inoltri = open("Inoltri.txt", "w")
t.addChannel("Inoltro", inoltri)

ricevuti = open("Ricevuti.txt", "w")
t.addChannel("Ricevuti", ricevuti)

# modello statistico di rumore
noise = open("meyer-light.txt", "r")
lines = noise.readlines()
for line in lines:
  str = line.strip()
  if (str != ""):
    val = int(str)
    for i in range(1,num_nodi+1):
      t.getNode(i).addNoiseTraceReading(val)    # aggiungo al nodo la misurazione del rumore

# creo il modello di rumore per il nodo
for i in range(1, num_nodi+1):
  t.getNode(i).createNoiseModel()   

#faccio partire i nodi
for i in range(1, num_nodi+1):
    t.getNode(i).bootAtTime(10000 + (num_nodi-i)*5)

#genero un certo numero di eventi al simulatore
for i in range(0, 200000):
  t.runNextEvent()

