import sys
import numpy as np
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
print(error)
