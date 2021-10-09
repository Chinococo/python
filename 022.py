def n(i):
    if(i==1):
        return 1
    return i * n(i-1)
print(n(int(input())),end='')