import random


def judge(table):
    win = [(0, 1, 2,), (0, 3, 6,), (0, 4, 8,), (1, 4, 7,), (2, 5, 8,), (3, 4, 5,), (6, 7, 8,), (2, 4, 6,)]
    for i in range(8):
        if table[win[i][0]]==table[win[i][1]]==table[win[i][2]] and table[win[i][0]]!=0:
            return True
    return  False
def output(table):
    for i in range(3):
        for x in range(3):
            print(table[i*3+x],end='')
        print()
def main():
    table = [0 for i in range(9)]
    round = 1
    turn = 0
    lst = []
    while (not judge(table) and round <= 9):
        table[int(input())] = turn % 2 + 1
        turn += 1
        output(table)
        print()
    turn += 1
    print('player', turn % 2 + 1, 'win')
    pass
if __name__ == '__main__':
    for i in range(1000):
        main()