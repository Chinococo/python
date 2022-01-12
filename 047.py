def main():
    n1,m1 = map(int,input().split())
    artice = []
    for i in range(n1):
        artice.append(input())
    for x in range(m1):
        cmd = input()
        if 'ADD_W_FRONT' in cmd:
            i,n,word = cmd.split()[1:]
            artice[int(i)-1] = add_fornt(artice[int(i)-1],int(n)-1,word)
        elif 'ADD_W_AFTER' in cmd:
            i, n, word = cmd.split()[1:]
            # print(artice[int(i) - 1])
            artice[int(i) - 1] = add_fornt(artice[int(i) - 1], int(n), word)
        elif  'ADD_S_FRONT'  in cmd:
            i,sentense = cmd.split()[1:]
            artice[int(i)-1]= sentense+' ' +artice[int(i)-1]
        elif  'ADD_S_AFTER'  in cmd:
            i, sentense = cmd.split()[1:]
            artice[int(i)-1]+=' '+sentense
        elif 'INSERT_FRONT' in cmd:
            key,word = cmd.split()[1:]
            for i in range(len(artice)):
                artice[i] = artice[i].replace(key,word+' '+key)
        elif 'INSERT_AFTER' in cmd:
            key,word = cmd.split()[1:]
            for i in range(len(artice)):
                artice[i] = artice[i].replace(key,key+' '+word)
        elif 'DEL_W' in cmd:
            i,n = map(int,cmd.split()[1:])
            artice[i-1] = delte(artice[i-1],n-1)
        elif  'DEL_L' in cmd:
            i = int(cmd.split()[1])
            artice.pop(i-1)
        elif 'REPLACE' in cmd:
            old,new = cmd.split()[1:]
            for i in range(len(artice)):
                artice[i] = artice[i].replace(old,new)
        else:
            c=0
            for i in range(len(artice)):
                c += len(artice[i].split())
            print(c)
        #output(artice)
    output(artice)
def add_fornt(s,n,word):
    t = s.split()
    t.insert(n,word)
    #print(t)
    return ' '.join(t)
def output(artice):
    for i in range(len(artice)):
        print(artice[i])
    #print()
def delte(s,i):
    t = s.split()
    t.pop(i)
    return ' '.join(t)
if __name__ == '__main__':
    main()