#! /usr/bin/python
import numpy as np
import math

def distanza(p1, p2):
    x = (p1[0]-p2[0])**2
    y = (p1[1]-p2[1])**2
    return math.sqrt(x+y)

def generaTopologia(n):
    x = np.random.rand(n)*100
    print("X: "+str(x)+"\n")
    y = np.random.rand(n)*100
    print("Y: "+str(y)+"\n")
    #z = np.random.rand(1)*20 - 60;
    punti = map(lambda a,b: (a,b), x, y)
    print("Punti: "+str(punti)+"\n")
    topo = []
    for i in range(0,len(punti)):
        for j in range(i+1, len(punti)):
            if (distanza(punti[i], punti[j]) <= 10):
                topo = topo + [(i+1, j+1, np.random.rand(1)[0]*20-60)]
                topo = topo + [(j+1, i+1, np.random.rand(1)[0]*20-60)]
    print("topo: "+str(topo)+"\n")
    return (punti, topo)




#t = open("topo_param.txt", "r")
#lines = t.readlines()
#num_nodi = int(lines[0])

(punti, nodi) = generaTopologia(200)

f = open("topo.txt", "w")
for ele in nodi:
   f.write(str(ele[0]) + ' ' + str(ele[1]) + ' ' + str(ele[2]) + '\n')
f.close()
