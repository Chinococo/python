line = int(input())
for i in range(0,line):
    print('#'*(line+i),end='');
    for k in range(line-i,0,-1):
        print(k,end='')
    if(i!=line-1):
        print()