#! /usr/bin/python

import matplotlib.pyplot as plt

f = open("risultatiK8.txt", "r")

lines = f.readlines()

xs = range(50, 250, 50)

arr1 = map(lambda x: float(x), lines[0].split())
plt.plot(xs, arr1, label='forwarded messages', marker='o')

arr2 = map(lambda x: float(x), lines[1].split())
plt.plot(xs, arr2, label='received messages', marker='^')

arr3 = map(lambda x: float(x), lines[2].split())
plt.plot(xs, arr3, label='trashed messages', marker='s')


plt.title('graph K=8')
plt.grid(True)
plt.xlim([50, 250])
plt.xlabel('number of nodes')
plt.ylabel('messages')


plt.legend(loc='upper left')

plt.show()

