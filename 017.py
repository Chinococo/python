index = int(input())
line  = int(input())

if(index==1):
    for i in range(int(line/2)+1):
        print('*'*(i+1))
    for i in range(int(line / 2),0,-1):
        print('*' * (i ))
elif index==2:
    for i in range(int(line/2)+1):
        print('.'*(int(line/2)-i),end='')
        print('*' *  (i+1) )
    for i in range(int(line / 2), 0, -1):
        print('.'*(int(line/2)-i+1),end='')
        print('*' *  (i) )
else:
    for i in range(int(line/2)+1):
        print('.'*(int(line/2)-i),end='')
        print('*' *  (i*2+1) )
    for i in range(int(line / 2), 0, -1):
        print('.' * (int(line / 2) - i+1), end='')
        print('*' * ((i-1) * 2+1 ))

''''
elif(index==2):
    for i in range(line, -line + 1, 1):

else:
    for i in range(line, -line + 1, 1):

'''''

