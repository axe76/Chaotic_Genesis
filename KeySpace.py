# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:38:03 2020

@author: ACER
"""
import math
import random
'''
d = 0.3
a = 2.5

x=[]
x.append(0.3)
y = []
y.append(0.2)

for i in range(10):
    x.append((x[i]+d+(a*math.sin(2*math.pi*y[i])))%1)
    y.append(1 - a*pow(x[i],2) + y[i])


str1 = [67,63,75,64]
str2 = [64,69,69,70]
str1 = set(str1)
str2 = set(str2)'''

def chaotic_map(n,x_0,y_0,a,d):
    # d = 0.3
    # a = 2.5 
    x=[]
    x.append(x_0)
    y = []
    y.append(y_0)

    for i in range(n-1):
        x.append((x[i]+d+(a*math.sin(2*math.pi*y[i])))%1)
        y.append(1 - a*pow(x[i],2) + y[i])

    return (x,y)

text = 'abcdefghij'
ascii_lst = [ord(i) for i in text]
n = len(text)
ascii_avg = sum(ascii_lst)/n
x_0 = ascii_avg/max(ascii_lst)
y_0 = 1-x_0
a = random.uniform(1,4)
d = random.uniform(0.1,4)
(x1,y1) = chaotic_map(n, x_0, y_0, a, d)

a1 = a#+ 10**(-15)
d1 = d#+ 10**(-15)
x_01 = x_0# + 10**(-16)
y_01 = y_0# - 10**(-16)

(x2,y2) = chaotic_map(n, x_01, y_01, a1, d1)

if(x1 == x2 or y1==y2):
    print('same')
else:
    print('diff')


