# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random#can I make a random number generator
import numpy#It should  be relatively easy to have python per
                #perform this without the package?
import matplotlib.pyplot as plt
rand2 = []
rand3 = []

#print(randList)
rand1 = random.randint(0,91)
#print(rand1)

for num in range(10):
    rand3 = random.randint(0,90)
    print(rand3)
    rand2.append(rand3)
    #print rand2

b = numpy.sin(rand2)
c = numpy.cos(rand2)  
print (b,c)

#Making plot magic

xAxis = numpy.arange(0,10,1)

fig, ax = plt.subplots()
#I don't know what fig does here
ax.plot(xAxis,b, 'o-', label='sin')
ax.plot(xAxis,c, '.-', label = 'cos')

plt.xlabel('Random Integer Number')
plt.ylabel('Trig operation')
legend = ax.legend(loc='upper center', shadow=True, fontsize = 'x-large')

#legend.get_fram().set_facecolor('00FFCC')

plt.show()

"""Informal Bibliography
look up the youtube tutorials
matplotlib.org specificall #matplotlib.pyplot.legend .subplot
"""

