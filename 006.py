A = str(input())
b = str(input())
x = str(input())
y = str(input())
c = A + b

d = c.replace(x, y)

#print(c)
#print(d)
print(len(c) + len(d))
print(str(d[0:3] + d[len(d) - 3:len(d)]) * 3,end='')
