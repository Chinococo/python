import math
falg = True
i  = int(input())
for k in range(2,int(math.sqrt()+1)):
    if(i%k==0):
        print('is not prime',end='')

print('prime',end='')