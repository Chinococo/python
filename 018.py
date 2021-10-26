def f1(n):
    # print(n)
    print(*list(range(1, n)) + list(range(n, 0, -1)), sep='')


def f2(n, line):
    print('_' * (line - n), *list(range(1, n)) + list(range(n, 0, -1)), '_' * (line - n), sep='')


def f3(n, line):
    print('_' * (n-1), *list(range(1, line-n+1)) + list(range(line-n+1, 0, -1)), '_' * (n-1), sep='')


def main():
    index = int(input())
    line = int(input())
    if (index == 1):
        for i in range(1, line + 1):
            f1(i)
    elif (index == 2):
        for i in range(1, line + 1):
            f2(i,line)
    else:
        for i in range(1, line + 1):
            f3(i,line)


if __name__ == '__main__':
    main()
