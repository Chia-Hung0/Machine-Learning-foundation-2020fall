import sys
import numpy as np
import random
import math
from numpy.linalg import inv
from numpy.linalg import multi_dot
in_filename = sys.argv[1]
fin = open(in_filename, 'r')
data = np.loadtxt(fin)
padding = np.full((1000, 1), 1)
fin.close()
data = np.append(padding, data, axis = 1)
x = data[0:1000 , :11]
y = data[0:1000 , 11:12]
xt = x.transpose()
xr = np.dot(xt, x)
xin = inv(xr)
Wlin = multi_dot([xin, xt, y])      
reg = np.dot(x, Wlin)
err = reg - y        
error = np.vdot(err, err)/1000
w = np.zeros((1, 11))
def SGDRegression(w, x, y):
    j = 0
    e = 1
    while e > 1.01 * error:
        k = random.randint(0, 999)
        xn = x[k, :11]
        yn = y[k]
        check = np.vdot(w, xn)
        w = w + 0.001 * 2 * (yn - check) * xn 
        j = j+1
        r = np.dot(x, w.transpose())
        er = r - y 
        e = np.vdot(er, er)/1000
    return j
iternum = 0
for i in range(1000):
    num = SGDRegression(w, x, y)
    iternum = iternum + num
print(iternum/1000)