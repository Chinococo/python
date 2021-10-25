def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return int((a*b)/gcd(a,b))
def main():
    line = input()
    a = int(line.split()[0])
    b = int(line.split()[1])
    c = int(line.split()[2])
    d = int(line.split()[3])
    e = int(line.split()[4])
    f = int(line.split()[5])
    ans=0
    t = lcm(a,c)
    k = lcm(a,c)
    while(t%e!=f):
        t+=k
    ans+=t

    t = lcm(a, e)
    k = lcm(a, e)
    while (t % c != d):
        t += k
    ans += t

    t = lcm(c, e)
    k = lcm(c, e)
    while (t % a != b):
        t += k
    ans += t
    while ans - a*c*e>0:
        ans-= a*c*e
    print(ans)
if __name__ == '__main__':
    main()