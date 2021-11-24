def main():
    Key = input().split()
    val = input().split()
    dict1 = {}
    for i in range(len(Key)):
        dict1[Key[i]] = int(val[i])
    dict1 = sorted(dict1.items(), key=lambda item: int(item[1]))
    for i in dict1:
        print(i[0], end='')


main()
