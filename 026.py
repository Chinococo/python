def tran(s):
    a = ''
    if s>0:
        a+='+'
    return a+str(s)
card = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 0.5, 'Q': 0.5, 'K': 0.5}
n = int(input())#人數
player = [int(i) for i in input().split()]
score = [card[i] for i in input().split()]
force = [False for i in range(n)]
for i in range(n):
    t =0
    while True:
        cmd = input()
        if(cmd=='N'):
            break
        score[i]+=card[input()]
        if(t==3 or score[i]>10.5 or (t==0 and score[i]==10.5)):
            if ((t==0 and score[i]==10.5) or t==3 ):
                force[i]=True
            break
        t += 1

judge = 0
judge += card[input()]
while True:
    cmd = input()
    if (cmd == 'N'):
        break
    judge += card[input()]
    if (judge >= 10.5):
        break

for i in range(n):
    if score[i]>10.5 or (judge<=10.5 and score[i]<=10.5 and judge>=score[i]):
        if(force[i]==False):
            player[i] = - player[i]
bank = 0
for i in range(n):
    bank += -player[i]
    print('Player{0} {1}'.format(i+1,tran(player[i])))
print('Bank {0}'.format(tran(bank)))






