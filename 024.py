
def check(i):
    c = True
    for k in range(len(i)-1):
        c = c and int(i[k])<=int(i[k+1])
    return c
def output():
    input1 = input()
    a = 0
    prev=0
    for i in range(0,len(input1)):
        for k in range(prev,int(input1[i])):
            a = a + list1[len(input1)-i][k]
        prev = int(input1[i])
    return a-int(not check(input1))




