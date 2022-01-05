ans = []
def bfs(dir,now_queue,prepath_queue,Y,t):
    next_queue=list()
    next_prepath_queue = list()
    for index in range(len(now_queue)):
        now = now_queue[index]
        if now == Y:
            for x in prepath_queue[index]:
                ans.append(str(x))
            if t == False:
                ans.remove(str(Y))
            #print(prepath_queue[index])
            return prepath_queue[index].copy()
        for i in range(len(dir[now])):
            if not dir[now][i] in prepath_queue[index]:
                t2 = prepath_queue[index].copy()
                t2.append(dir[now][i])
                next_queue.append(dir[now][i])
                next_prepath_queue.append(t2)
    #print(next_queue)
    if len(next_queue)!=0:
        bfs(dir,next_queue,next_prepath_queue,Y,t)
    else:
        return  list().copy()
def main():
    N,X,Y,Z = map(int,input().split())
    dir = dict()
    for i in range(N):
        x,y = map(int,input().split())
        if not x in dir:
            dir[x]=list()
        if not y in dir :
            dir[y]=list()
        dir[x].append(y)
        dir[y].append(x)
    bfs(dir, [X], [[X]], Y,False)
    bfs(dir, [Y], [[Y]], Z,True)

    if ans[-1]==str(Z):
        print(len(ans)-1)
        print("-".join(ans))
    else:
        print('No way!')

if __name__ == '__main__':
    main()