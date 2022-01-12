room = []
metting = []
temp = []
ans = []
def dfs(index):
    if index == len(metting):
        #print(temp)
        j = judge()
        if j != (-1,-1):
            #print(j)
            ans.append(j[1])
        return
    temp.append(('',0,))
    dfs(index+1)
    temp.pop()  
    for i in range(len(room)):
        #print(room[i][1],metting[index][2])
        if room[i][1]>=metting[index][2]:
            temp.append((room[i][0],1,))
            dfs(index+1)
            temp.pop()
def judge():
    use_room = 0
    use_time = 0
    for i in range(len(room)):
        chs = []
        u = 0
        for x in range(len(temp)):
           if temp[x][0]==room[i][0] and temp[x][1]==1 :
               chs.append(x)        
        now = [0,0]
        
        for x in range(len(chs)):
            if now[1]<=metting[chs[x]][0]:
               use_time +=  metting[chs[x]][1]-metting[chs[x]][0]
               u += metting[chs[x]][1]-metting[chs[x]][0]
               now = metting[chs[x]][:2]
            else:   
                return (-1,-1,)

        if not now[0]==now[1]==0:
            use_room+=1
            #print(room[i][0],u)
        #print(room[i][0],chs,u)    

    return (use_room,use_time,)          
def main():
    n,m = map(int,input().split())
    for i in range(n):
        line =  list(map(int,input().split()))
        room.append(line)     
    for i in range(m):
        line = list(map(int,(input().split())))
        metting.append((line[2],line[3],line[1],line[0],))
    #print(metting)
    dfs(0)
    ans.append(0)
    ans.sort()
    
    print(ans[-1])
main()    
        
