name = input()
m    = float(input())
m = m/100
kg = float(input())
bmi = kg/pow(m,2)
print('Hi {}, Your BMI: {:f}'.format(name,bmi),end='')
if(bmi<18.5):
    print(' too LOW',end='')
elif(bmi>24):
    print(' too HIGH',end='')
print('.',end='')
