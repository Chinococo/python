from math import factorial as fc


def main():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(eval, input().split())))

    ma = fc(n) / fc(n - 3)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                a = m(lst[i], lst[j])
                b = m(lst[j], lst[k])
                if (a == b):
                    print(lst[i], lst[j], lst[j])
                    ma -= 1
    print(int(ma))


def m(p, q):
    if ((p[0] - q[0]) == 0):
        return "h"
    return abs(p[1] - q[1]) / (p[0] - q[0])


main()