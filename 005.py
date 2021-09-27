article = str(input())
p = str(input())
q = str(input())
list1 = article.split(' ')
list2 = article.split(' ')
list3 = article.split(' ')
for i in range(len(list1)):
    if(list1[i]==p):
        list1[i] = q
for i in range(len(list1)):
    print(list1[i],end='')
    if(i!=len(list1)-1):
        print(' ',end='')
print('')
for i in range(len(list2)):
    if(list2[i]==p):
        list2.insert(i,q)
for i in range(len(list2)):
    print(list2[i],end='')
    if(i!=len(list2)-1):
        print(' ',end='')

print('')
for i in range(len(list3)):
    if(i==len(list3)):
        break
    if(list3[i]==p):
        del(list3[i])
        i = i-1
for i in range(len(list3)):
    print(list3[i],end='')
    if(i!=len(list3)-1):
        print(' ',end='')
