dic = {'S': 3, 'H': 2, 'D': 1, 'C': 0}
card = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}


def main():
    list = input().split()
    list1 = []
    list2 = []
    s1 = set()  # 點數
    s2 = set()  # 符號

    for i in range(len(list)):
        # print(list[i][:-1], list[i][-1])
        s1.add(card[list[i][:-1]])
        s2.add(dic[list[i][-1]])
        list1.append(card[list[i][:-1]])
        list2.append(dic[list[i][-1]])
    list1.sort()
    list1 = list1 + [(x + 13) for x in list1]
    if (len(s1) == 5 and len(s2) == 1):
        for s in range(5):
            if list1[s + 4] - list1[s] == 4:
                return 8
    if (len(s1) == 2):
        count = 0
        for s in range(5):
            if list1[0] == list1[s]:
                count += 1
        if (count == 1 or count == 4):
            return 7
    if (len(s1) == 2):
        count = 0
        for s in range(5):
            if list1[0] == list1[s]:
                count += 1
        if (count == 3 or count == 2):
            return 6
    if (len(s2) == 1):
        return 5
    if (len(s1) == 5):
        for s in range(5):
            if list1[s + 4] - list1[s] == 4:
                return 4
    count = 0
    for s in range(3):
        if list1[s] == list1[s + 1] == list1[s + 2]:
            count += 1
        if count == 1:
            return 3

    count = 0
    for s in range(4):
        if list1[s] == list1[s + 1]:
            count += 1
        if count == 2:
            return 2

    count = 0
    for s in range(4):
        if list1[s] == list1[s + 1]:
            count += 1
    if count == 1:
        return 1
    return 0


if __name__ == '__main__':
    print(main())
