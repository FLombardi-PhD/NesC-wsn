#! /usr/bin/python

import matplotlib.pyplot as plt

f = open("risultatiK8.txt", "r")

lines = f.readlines()

xs = range(50, 250, 50)
#xs = map(lambda x: x+50, xs)


arr1 = map(lambda x: float(x), lines[0].split())
plt.plot(xs, arr1, label='Messaggi Inviati', marker='o')

arr2 = map(lambda x: float(x), lines[1].split())
plt.plot(xs, arr2, label='Messaggi Ricevuti', marker='^')

arr3 = map(lambda x: float(x), lines[2].split())
plt.plot(xs, arr3, label='Messaggi Scartati', marker='s')


plt.title('grafico K=8')
plt.grid(True)
plt.xlim([50, 250])
plt.xlabel('Numero nodi')
plt.ylabel('Messaggi')


plt.legend(loc='upper left')

plt.show()

