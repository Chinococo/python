s = ['~','!','@','#','$','%','^','&','*','<','>','_','+','=']
def count(s):
    c = 0
    list1=[]
    for i in range(len(s)):
        if s[i].islower():
            c += 1
        elif s[i].isupper():
            c += 2
        elif s[i].isdigit() :
            list1.append(i)
            c += 3
        elif s[i] in s:
            c += 5
    m=1
    for i in range(1,len(list1)):

       if(list1[i]-list1[i-1]>1):
           m+=1
           if(m>=5):
               c+=10
               break
       else:
           m=1


    return c


mi = 100000
strmi = ''
ma = -1
strma = ''

while True:
    line = input()
    if (line == '-1'):
        break
    if mi > count(line):
        mi = count(line)
        strmi = line
    if ma < count(line):
        ma = count(line)
        strma = line

print(strma, ma)
print(strmi, mi)
