from math import sqrt

a = int(input())
b = int(input())
c = int(input())
x1 =  ((-b)+sqrt(b*b-4*a*c))/(2*a)
x2 =  ((-b)-sqrt(b*b-4*a*c))/(2*a)
print('{:.1f}'.format(x1))
print('{:.1f}'.format(x2))
