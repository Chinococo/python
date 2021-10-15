import sys


def check(i):
    c = True
    for k in range(len(i)-1):
        c = c and int(i[k])<=int(i[k+1])
    return c


def main():
    list1 = [[1] + [0] * 9, [1] * 10]
    for k in range(2, 100002):
        prev = [0] * 11
        for i in range(9, -1, -1):
            prev[i] = (prev[i + 1] + list1[k - 1][i])% (1000000007)
        list1.append(prev)
    for line in sys.stdin:
        input1 = str(line).strip()
        prev = 0
        a=0
        len_input1 = len(input1)
        for i in range(0, len_input1):
            for k in range(prev, int(input1[i])):a = a + list1[len_input1 - i][k]
            a = a% (1000000007)
            if (int(input1[i]) >= prev):prev = int(input1[i])
            else:break
        print(a - int(not check(input1)) % (1000000007))

if __name__ == '__main__':
    main()

