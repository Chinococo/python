def k(n):
    if n==0 or n==1:
        return n
    return 2*k(n-1)+3*k(n-2)
def  main():
    a = input()
    if a.isnumeric() :
        if 2 <= int(a):
            print(k(int(a)))
            return
    print('Error')
main()