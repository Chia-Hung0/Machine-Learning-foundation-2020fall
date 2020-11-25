import sys
import numpy as np
from numpy.linalg import inv
from numpy.linalg import multi_dot
def Qtransform(A, Q):
    a = A[0:A.shape[0], 0:1]
    b = A[0:A.shape[0], 1:11]
    c = A[0:A.shape[0], 11:12]
    for i in range(Q):
        paste = np.power(b, i+1)
        a = np.concatenate((a, paste), axis=1)
    a = np.concatenate((a, c), axis=1)
    return a
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
data = Qtransform(data, 10)
test = Qtransform(test, 10)
x = data[0:1000 , 0:101]
y = data[0:1000 , 101:102]
xt = x.transpose()
xr = np.dot(xt, x)
xin = inv(xr)
Wlin = multi_dot([xin, xt, y])  
xtest = test[0:3000 , 0:101]
ytest = test[0:3000 , 101:102]       
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