n = int(input())
list1 = []
while(n>0):
    n = n-1
    list1.append(int(input()))
list1.sort()
print(list1[-2])
print(list1[0]*list1[-1],end='')
