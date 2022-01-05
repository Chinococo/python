def main():
    n = int(input())
    data = dict()
    ans = dict()
    for i in range(n):
        school,list1 = input().split()
        data[school] = list1
        ans[school]=0
    list1 = [[] for i in range(n+1)]

    conditon = input().split('+')
    for x in conditon:
        for eleme in data:
            for need in x.split():
            list2 = x.split()
        


if __name__ == '__main__':
    main()