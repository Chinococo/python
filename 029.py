def main():
    A = map(int,input().split())
    A = sorted(A,key=lambda n:(n%2==0,n%2 and n,-n))
    print(A)
main()
