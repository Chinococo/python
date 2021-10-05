index = int(input())
line  = float(input())
line  = int(-line/2)

if(index==1):
    for i in range(line,-line+1,1):
        print('*'*((-line+1)-abs(i)))
elif(index==2):
    for i in range(line, -line + 1, 1):
        print('.' *  abs(i)+'*' * ((-line+1) - abs(i)))
else:
    for i in range(line, -line + 1, 1):
        print('.' * (abs(i)) + '*' * (((-line + 1) - abs(i))*2-1))
