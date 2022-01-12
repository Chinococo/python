def judge(lst):
    check=[(1,2,3,),(4,5,6,),(7,8,9,),(1,4,7,),(2,5,8,),(3,6,9,),(1,5,9,),(3,5,7,)]
    for i in range(8):
        if lst[check[i][0]]==lst[check[i][1]]==lst[check[i][2]] and lst[check[i][0]]!=0:
            return lst[check[i][0]]
    return 0        
def main():
    lst = [0 for i in range(10)]
    now = int(input())
    line = list(map(int,input().split()))
    result = -1
    satue = True
    if len(set(line))==len(line):
        print('OK')
    else:
        print('Error')
    
    before = []  

    for i in range(len(line)):
       
        if line[i] not in before:
            #print(now,line[i])
            lst[line[i]]=now;
        else:
            continue    
        before.append(line[i])
        j = judge(lst)
        if j != 0:
            result = now
            break
        now = 1 if now == 2 else 2
   
    for i in range(1,10,3):
        print(' '.join(list(map(str, lst[i:i+3]))))
    if result == 1:
        print('Player win')
    elif result == 2:
        print('Computer win')
    elif len(line) == 9 :
        print('Tie')
    else:
        print('Undecided')
        for i in range(1,10):
            if lst[i]==0 :
                lst[i]=2
                if judge(lst)==2:
                    print(i)
                    return  
                lst[i]=0 
        for i in range(1,10):
            if lst[i]==0 :
                lst[i]=1
                if judge(lst)==1:
                    print(i)
                    return
                lst[i]=0    
                    


main()