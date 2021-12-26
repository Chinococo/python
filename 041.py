def bfs(list2,target,queue,record):
    next = []
    re = []
    for i in range(len(queue)):
        if target==queue[i]:
            print('Yes!')
            return
        for index in range(len(list2[queue[i]])):
            if list2[queue[i]][index] not in record:
                re = record.copy()
                re.append(queue[i])
                next.append(list2[queue[i]][index])
    if len(queue)==0:
        print('No!')
    else:
        #print(next)
        bfs(list2,target,next,re)

def main():
    n,x,y= map(int,input().split())
    list1 = [[] for i in range(1000000)]
    for i in range(n):
        x1,y1=map(int,input().split())
        list1[x1].append(y1)
        list1[y1].append(x1)
    queue = []
    record = []
    for i in range(len(list1[x])):
        queue.append(list1[x][i])
        record.append(set())
    bfs(list1,y,queue,record)

if __name__ == '__main__':
    main()