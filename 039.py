def mess1(ans, s1, set1: set, val: list,n):
    if len(val) == n:
        val.sort()
        s = ''
        for i in range(len(val)):
            s+=s1[val[i]]
        ans.add(s)
        return
    for i in range(len(s1)):
        if not s1[i] in set1:
            set2 = set1.copy()
            set2.add(s1[i])
            val2 = val.copy()
            val2.append(i)
            mess1(ans, s1, set2, val2,n)

def main():
    s1,n = input().split()
    n = int(n)
    ans = set()
    mess1(ans,s1,set(),[],n)
    print(' '.join(sorted(ans)))

if __name__ == '__main__':
    main()