import sys
import numpy as np
from numpy.linalg import inv
from numpy.linalg import multi_dot
in_filename1 = sys.argv[1]
in_filename2 = sys.argv[2]
fin = open(in_filename1, 'r')
data = np.loadtxt(fin)
padding1 = np.full((1000, 1), 1)
padding2 = np.full((3000, 1), 1)
fin.close()
fin = open(in_filename2, 'r') 
test = np.loadtxt(fin)
data = np.append(padding1, data, axis = 1)
test = np.append(padding2, test, axis = 1)

x = data[0:1000 , :11]
y = data[0:1000 , 11:12]
xt = x.transpose()
xr = np.dot(xt, x)
xin = inv(xr)
Wlin = multi_dot([xin, xt, y])      
xtest = test[0:3000 , :11]
ytest = test[0:3000 , 11:12]       
reg1 = np.dot(x, Wlin)
reg2 = np.dot(xtest, Wlin)
err1 = 0
err2 = 0
for i in range(1000):
    if reg1[i][0] * y[i][0] <0:
        err1 = err1 + 1
for i in range(3000):        
    if reg2[i][0] * ytest[i][0] <0:
        err2 = err2 + 1
print(abs(err1-err2/3)/1000)
fin.close()