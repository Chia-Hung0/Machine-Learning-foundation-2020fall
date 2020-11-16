import math
import random
import numpy as np
def h(s, theta, x):
    if s * (x - theta) > 0:
        return 1
    else:
        return -1
def Ein(size, s, theta, data, data2):
    err = 0
    for i in range(size):
        if h(s, theta, data[i][0]) != data[i][1]:
            err = err +1
    return err/size        
data_size = 2
tou = 0
Eoutin = []
for j in range(100000):
    data = []
    data1 = []
    data2 = [-1]
    for i in range(data_size):
        x = random.uniform(-1, 1)
        data.append((x, h(1, 0, x)))
        data1.append(x) 
    data.sort(key = lambda s: s[0])
    data1.sort()
    for i in range(data_size-1):
        data2.append((data1[i]+data1[i+1])/2)
    min_Ein = 1
    cur_s = 1
    cur_theta = -1
    for i in data2:
        s = -1
        if Ein(data_size, s, i, data, data2)<min_Ein:
            cur_s = s
            cur_theta = i
            min_Ein = Ein(data_size, s, i, data, data2)
        s = 1
        if Ein(data_size, s, i, data, data2)<min_Ein:
            cur_s = s
            cur_theta = i
            min_Ein = Ein(data_size, s, i, data, data2)
    if cur_s == 1:
        E = abs(cur_theta)/2
    else:
        E = (2-abs(cur_theta))/2 
    Eoutin.append(E - min_Ein)   
average = 0    
for i in Eoutin:
    average = average + i
average = average/100000
print('Eout-Ein = {}'.format(average))    
#print('s = {} theat = {} Ein = {} Eout={}'.format(cur_s, cur_theta, min_Ein, abs(cur_theta)/2))