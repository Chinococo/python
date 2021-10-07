def power(a,b):
    if(b==1):
        return a
    temp = power(a,b//2)
    if(b%2==1):
        return temp*temp*a
    else:
        return temp*temp


print(power(10,3))