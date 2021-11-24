def C(m):
    #print(m)
    if m==1 or m==0:
        return 0
    if m%2==0:
        return 1+C(m/2)
    return 1+C((m+1)/2)
def b2i(s):
    ans=0
    for i in range(len(s)):
        ans+=int(s[i])*2**(len(s)-1-i)
    return int(ans)
def i2b(s):
    ans=''
    while s>0:
        ans = ans + str(int(s%2))
        s = s//2
    while len(ans)<4:
        ans = ans + '0'    
    return ans[::-1]
def main():
    s = input()
    result = []
    while s!='-1':
        result.append(i2b(C(b2i(s))))
        s = input()
    print('\n'.join(result))
main()
