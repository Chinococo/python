def main():
    m,n = map(int,input().split())
    lst = []
    lst.append('dont use')
    for i in range(m):
        lst.append(input())
    copy=''    
    for i in range(n):
        cmd = input()
        if 'ADD_W_FRONT' in cmd:
            i,n= map(int,cmd.split()[1:3])
            word = cmd.split()[3]
            temp = lst[i].split()
            temp.insert(n-1,word)
            lst[i] = ' '.join(temp)

        elif 'ADD_W_AFTER' in cmd:
            i,n= map(int,cmd.split()[1:3])
            word = cmd.split()[3]
            temp = lst[i].split()
            temp.insert(n,word)
            lst[i] = ' '.join(temp)

        elif 'ADD_S_FRONT' in cmd:
            i= int(cmd.split()[1])
            word = ' '.join(cmd.split()[2:])
            lst[i] = word+' '+str(lst[i])

        elif 'ADD_S_AFTER' in cmd:
            i= int(cmd.split()[1])
            word = ' '.join(cmd.split()[2:])
            #print('test',lst[i]+' '+word)
            lst[i] = lst[i]+' '+word

        elif 'INSERT_FRONT' in cmd:
            key,word = cmd.split()[1:]
            for i in range(1,len(lst)):
                lst[i] = lst[i].replace(key,word+' ' +key)

        elif 'INSERT_AFTER' in cmd:
            key,word = cmd.split()[1:]
            for i in range(1,len(lst)):
                lst[i] = lst[i].replace(key,key+' '+word)

        elif 'DEL_W' in cmd:
            i,n= map(int,cmd.split()[1:])
            temp = lst[i].split()
            temp.pop(n-1)
            lst[i] = ' '.join(temp)    
        elif 'DEL_L' in cmd:
            i = int(cmd.split()[1])
            lst.pop(i)
        elif 'REPLACE' in cmd:
            old,new1 = cmd.split()[1:]
            for i in range(1,len(lst)):
                 lst[i] =  lst[i].replace(old,new1)
        elif 'COPY_L' in cmd:
            i= int(cmd.split()[1])
            copy = lst[i]
        elif 'COPY' in cmd:
            i,n= map(int,cmd.split()[1:]) 
            copy= lst[i].split()[n-1]
            
        elif 'PASTE_FRONT'  in cmd:   
            i,n= map(int,cmd.split()[1:]) 
            temp = lst[i].split()
            temp.insert(n-1,copy)
            lst[i] = ' '.join(temp)
        elif  'PASTE_AFTER' in cmd:
            i,n= map(int,cmd.split()[1:]) 
            temp = lst[i].split()
            temp.insert(n,copy)
            lst[i] = ' '.join(temp)   
        elif 'COUNT' in cmd:
            a= 0
            for i in range(1,len(lst)):
                a+=len(lst[i].split())
            print(a)
       
    for i in range(1,len(lst)):
        print(lst[i])    
            
main()