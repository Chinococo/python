def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)    

def lcm(a,b):
    return (a*b)/gcd(a,b)

def find(Val,Mod,TargetMod):
    i = 1
    while (Val*i)%Mod!=TargetMod:
        i+=1
    return Val*i    

def main():
    
    x1,y1,x2,y2,x3,y3 =  map(int,input().split())
    #print(find(lcm(x2,x3),x1,y1))
    #print(find(lcm(x1,x3),x2,y2))
    #print(find(lcm(x1,x2),x3,y3))
    ans = find(lcm(x2,x3),x1,y1)+find(lcm(x1,x3),x2,y2)+find(lcm(x1,x2),x3,y3)
    while ans-lcm(lcm(x1,x2),x3)>0:
        ans-= lcm(lcm(x1,x2),x3)
    print(int(ans))

main()    