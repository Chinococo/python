
def main():

    s1,n =input().split()
    i = 0
    while i < len(s1):
        if s1[i].isalpha() == False:
            s1 = s1[:i]+s1[i+1:]
        else:
            i+=1
    #print(s1)
    s2=''
    for i in range(len(s1)):
        if s1[i].isupper():
            s2+=s1[i].lower()
        else:
            s2+=s1[i].upper()
    t = []
    n = int(n)
    for i in range(0,len(s2),n):
        t.append(s2[i:i+n])
    '''if not len(s2)%n==0:
        t.append(s2[int(len(s2)/n)*n:])'''
    t.reverse()
    print('/'.join(t))
if __name__ == '__main__':
    main()