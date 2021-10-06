dic = {'A': 1
    , '2': 2
    , '3': 3
    , '4': 4
    , '5': 5
    , '6': 6
    , '7': 7
    , '8': 8
    , '9': 9
    , '10': 10
    , 'J': 0.5
    , 'Q': 0.5
    , 'K': 0.5
       }
a = 0
b = 0
for i in range(3):
    a += dic[str(input())]
for i in range(3):
    b += dic[str(input())]
if (a > 10.5):
    a = 0
if (b > 10.5):
    b = 0
if (abs(10.5 - a) == abs(10.5 - b)):
    print('Tie', end='')
elif (abs(10.5 - a) > abs(10.5 - b)):
    print('B Win', end='')
else:
    print('A Win', end='')
