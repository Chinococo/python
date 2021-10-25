n = int(input())
list1 =[]
for i in range(n):
    line = input()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    list1.append([a,b])
list1.sort()
x = list1[0][0]
y = list1[0][1]
ans=0
for i in range(1,n):
    if(list1[i][0]<=y and list1[i][0]>=x):
        y = max(y,list1[i][1])
    else:
        ans += y-x
        x = list1[i][0]
        y = list1[i][1]
ans += y-x
print(ans)
