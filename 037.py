list = []
n = int(input())
for i in range(n):
    t = input().split(',')
    list.append((int(t[0]),int(t[1])))
list.sort()
x,y = list[0]
len1 = 0
for i in range(1,n):
    if x<=list[i][0]<=y:
        y = max(y,list[i][1])
    else:
        print(x,y,sep=',')
        x,y=list[i]
print(x,y,sep=',')