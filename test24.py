def main():
    dic = {"A": 1,
           "2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "10": 10,
           "J": 0.5,
           "Q": 0.5,
           "K": 0.5}

    pCnt = int(input())
    pIn = tuple(map(int, input().split()))

    card = [[dic[i]] for i in input().split()]
    point = [i[0] for i in card]
    money = [0 for i in range(pCnt)]
    card.append([])
    point.append(0)
    money.append(0)

    cur = 0
    while (cur <= pCnt):
        c = input()
        if (c == "Y"):
            continue
        elif (c == "N"):
            cur += 1
        else:
            card[cur].append(dic[c])
            point[cur] += dic[c]
            if (cur < pCnt):
                if (point[cur] > 10.5):
                    point[cur] = 0
                    money[cur] -= pIn[cur]
                    money[-1] += pIn[cur]
                    cur += 1
                elif (len(card[cur]) == 2 and (0.5 in card[cur]) and (10 in card[cur])):
                    money[cur] += pIn[cur]
                    money[-1] -= pIn[cur]
                    point[cur] = 0
                    cur += 1
                elif (len(card[cur]) == 5):
                    money[cur] += pIn[cur]
                    money[-1] -= pIn[cur]
                    point[cur] = 0
                    cur += 1

    for cur in range(pCnt):
        if (point[cur] != 0):
            if (point[-1] >= point[cur]):
                money[-1] += pIn[cur]
                money[cur] -= pIn[cur]
            else:
                money[-1] -= pIn[cur]
                money[cur] += pIn[cur]

                # print(card)
    # print(point)
    # print(money)
    for i in range(pCnt):
        print(f"Player{i + 1} " + ("+" if (money[i] > 0) else "") + f"{money[i]}")
    print("Bank " + ("+" if (money[-1] > 0) else "") + f"{money[-1]}")


main()