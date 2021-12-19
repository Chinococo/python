n=10
def robot(x, y, map):
    if x < 0 or x > n or y < 0 or y > n or map[x][y]==True:
        return
    else:
        map[x][y] = True
    robot(x + 1, y )
    robot(x - 1, y )
    robot(x, y + 1 )
    robot(x, y - 1 )

def main():
    List1 = [1 for i in range(101)]
    for i in range(3, 101):
        List1[i] = List1[i - 1] + List1[i - 2]
    input1 = int(input())
    while input1 != -1:
        print(List1[input1])
        input1 = int(input())


main()
