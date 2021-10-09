import array
import math
import numpy as np
test = np.zeros(2001,dtype=bool)
test[1]=True
for i in range(2,int(math.sqrt(2000)+1)):
    k=2
    if(test[k]==True):
        continue
    while i*k<=2000:
        test[i*k] = True
        k = k+1

input1 = int(input())
if(test[input1]==False):
    print('{} is prime number'.format(input1),end='')
else:
    print('{} is not prime number'.format(input1),end='')

