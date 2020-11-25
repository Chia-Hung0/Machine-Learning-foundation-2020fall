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
w = Wlin.transpose()
def SGDLogistic(w, x, y):
    e = 0
    for i in range(500):
        k = random.randint(0, 999)
        xn = x[k, :11]
        yn = y[k]
        check = np.vdot(w, xn)
        w = w + 0.001 * yn * xn * (1 / (1 + math.exp(yn * check)))
    for i in range(1000):
        xn = x[i, :11]
        yn = y[i]
        e = e + np.log(((1 + math.exp(-yn * np.vdot(w, xn)))))
    return e/1000
aver = 0
for i in range(1000):
    num = SGDLogistic(w, x, y)
    aver = aver + num
print(aver/1000)