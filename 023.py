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
a = 0.0
b = 0.0

a += dic[str(input())]
b += dic[str(input())]
computer = True
player   = True
while(player==True or computer==True):
    if(player==True):
        want = input()
        if(want=='Y'):
            a += dic[str(input())]
        else:
            player = False
    if (a > 10.5):
        a = 0
        player=False
    if(computer == True):
        if(b<a or b <= 8.0):
            b += dic[str(input())]
        else:
            computer=False
        if(b>10.5):
            b=0
            computer = False



if (a > 10.5):
    a = 0
if (b > 10.5):
    b = 0
print('{:.1f} vs. {:.1f}'.format(a,b))

if (abs(10.5 - a) == abs(10.5 - b)):
    print("It's a tie", end='')
elif (abs(10.5 - a) > abs(10.5 - b)):
    print('computer wins', end='')
else:
    print('player wins', end='')
