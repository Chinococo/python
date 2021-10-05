def cap1(t):
    return (t>='a') & (t<='z')
def cap2(t):
    return (t>='A') & (t<='Z')


artice = input()
artice.islower()
str1 =''
for i in range(len(artice)):
    if(cap1(artice[i])):
        str1+=artice[i]
if(str1 != ''):
    print(str1)
else:
    print('No lowercase letters')
print(len(artice))
count=0
for i in range(len(artice)):
    if(cap2(artice[i])):
        count = count+1
print(count,end='')