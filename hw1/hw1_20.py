import sys
import numpy as np
import random
in_filename = sys.argv[1]
fin = open(in_filename, 'r')
data = np.loadtxt(fin)
update = np.full((100, 1), 0)
data = np.append(update, data, axis = 1)
w = np.zeros((1, 11))
def perceptron(w, data):
    j = 0
    correct = 0
    while correct <500:
        k = random.randint(0, 99)
        x = data[k, :11]
        y = data[k, 11]/4
        check = np.dot(w, x)
        correct = correct + 1
        if(check * y <= 0):
            w = w + y * x
            j = j+1
            correct = 0
    return j
 
number = []

for i in range(1000):
    j = perceptron(w, data)
    number.append(j)  
number.sort()    
print((number[500]+number[499])/2)


fin.close()
