list1 = [0]
def dfs(data,sum,index,queue,prev,ban,d,maxd):
    if index>=len(data) :
        if d!=maxd:
            dfs(data,sum,0,[],0,ban.copy().union(queue),d+1,maxd)
        else:
            #print(ban)
            list1.append(sum)
        return
    if prev<=data[index][0] and not index in ban:
        t1 = queue.copy()
        t1.append(index)
        dfs(data,sum+data[index][1]-data[index][0],index+1,t1,data[index][1],ban,d,maxd)
    t1 = queue.copy()
    dfs(data,sum,index+1,t1,prev,ban,d,maxd)
def main():

    n,m = map(int,input().split())
    data = []
    for i in range(m):
        index,f,e = map(int,input().split())
        data.append((f,e,))
    data.sort()
    dfs(data,0,0,[],-1,set(),1,n)
    list1.sort()
    print(list1[-1])
if __name__ == '__main__':
    main()