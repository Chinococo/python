index = int(input())
line  = int(input())

if(index==1):
    for i in range(1,line+1):
        list1 = list(range(1,abs(i)+1))
        print(''.join('%s' %id for id in list1))
