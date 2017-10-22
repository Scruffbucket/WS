#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:46:03 2017

@author: Apollo
"""
import matplotlib.pyplot as plt

a =[]
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []
t = []
u = []
v = []
w = []
x = []
y = []
z = []
fullList = []

with open("sample.txt") as fileobj:
    for line in fileobj:
        for ch in line:
            if ch == 'a':
                a.append('a')
            elif ch == 'b':
                b.append('b')
            elif ch == 'c':
                c.append('c')
            elif ch == 'd':
                d.append('d')
            elif ch == 'e':
                e.append('e')
            elif ch == 'f':
                f.append('f')
            elif ch == 'g':
                g.append('g')
            elif ch == 'h':
                h.append('h')
            elif ch == 'i':
                i.append('i')
            elif ch == 'j':
                j.append('j')
            elif ch == 'k':
                k.append('k')
            elif ch == 'l':
                l.append('l')
            elif ch == 'm':
                m.append('m')
            elif ch == 'n':
                n.append('n')
            elif ch == 'o':
                o.append('o')
            elif ch == 'p':
                p.append('p')
            elif  ch == 'q':
                q.append('q')
            elif ch == 'r':
                r.append('r')
            elif ch == 's':
                s.append('s')
            elif ch == 't':
                t.append('t')
            elif ch == 'u':
                u.append('u')
            elif ch == 'v':
                v.append('v')
            elif ch == 'w':
                w.append('w')
            elif ch == 'x':
                x.append('x')
            elif ch == 'y':
                y.append('y')
            elif ch == 'z':
                z.append('z')
            #print (ch)
            
fullList.append(len(a))
fullList.append(len(b))
fullList.append(len(c))
fullList.append(len(d))
fullList.append(len(e))
fullList.append(len(f))
fullList.append(len(g))
fullList.append(len(h))
fullList.append(len(i))
fullList.append(len(j))
fullList.append(len(k))
fullList.append(len(l))
fullList.append(len(m))
fullList.append(len(n))
fullList.append(len(o))
fullList.append(len(p))
fullList.append(len(q))
fullList.append(len(r))
fullList.append(len(s))
fullList.append(len(t))
fullList.append(len(u))
fullList.append(len(v))
fullList.append(len(w))
fullList.append(len(x))
fullList.append(len(y))
fullList.append(len(z))
#print(fullList)
            
"""sample code from problem 1
xAxis = numpy.arange(0,len(fullList),1)
#I don't know what fig does here
ax.plot(xAxis,b, 'o-', label='sin')
ax.plot(xAxis,c, '.-', label = 'cos')

plt.xlabel('Random Integer Number')
plt.ylabel('Trig operation')
legend = ax.legend(loc='upper center', shadow=True, fontsize = 'x-large')

legend.get_fram().set_facecolor('00FFCC')

plt.show()
plt.scatter()
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75n)
"""

letters = [x for x in range(len(fullList))]
plt.bar(letters,fullList)

plt.xlabel('Letters')
plt.ylabel('Frequency')
plt.title('Frequency of letters')
plt.axis([-1,26,0,30])
#plt.grid(True)
plt.show







