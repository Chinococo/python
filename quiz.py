card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
score =[1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
def sc():
    return score[card.index(str(input()))]+score[card.index(str(input()))]+score[card.index(str(input()))]
a=0.0
b=0.0
a=sc()
b=sc()
if(a>10.5):
    a = 0
if (b > 10.5):
    b = 0
if(abs(10.5-a)==abs(10.5-b)):
    print('Tie',end='')
elif (abs(10.5-a)>abs(10.5-b)):
    print('B Win',end='')
else:
    print('A Win',end='')
