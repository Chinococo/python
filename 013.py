m = int(input())
n = int(input())
t = 0
for i in range(m,n,2):
    t = t+i
print(t)
t = 1
for i in range(m,n,3):
    t = t*i
print(t,end='')
