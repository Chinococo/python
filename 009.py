a = int(input())
b = int(input())
c = int(input())
ans = 0
if(a<=10):
    ans += (a*30)*1
elif(a<=15):
    ans += (a*30)*0.95
elif(a<=20):
    ans += (a*30)*0.9
else:
    ans += (a*30)*0.8

if(b<=10):
    ans += (b*70)*1
elif(b<=15):
    ans += (b*70)*0.9
elif(b<=20):
    ans += (b*70)*0.85
else:
    ans += (b*70)*0.75

if(c<=10):
    ans += (c*40)*1
elif(c<=15):
    ans += (c*40)*0.85
elif(c<=20):
    ans += (c*40)*0.8
else:
    ans += (c*40)*0.8
if(a+b+c>=30):
    ans*= 0.87
print(int(ans),end='')
