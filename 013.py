m = int(input())
n = int(input())
t = 0
for i in range(m,n+1,2):
    t = t+i
print(t)
t = 1
for i in range(m,n+1,3):
    t = t*i
print(t,end='')
