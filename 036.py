def a(n):
    if n==1 or n==2:
        return 2*n
    return a(n-1)+n
print(a(5))