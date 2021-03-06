def bfs(list2,target,queue,record):
    next = []
    re = list()
    for i in range(len(queue)):
        if target==queue[i]:
            print('Yes!',end='')
            return
        for index in range(len(list2[queue[i]])):
            if list2[queue[i]][index] not in record[i]:
                t = record[i].copy()
                t.add(queue[i])
                re.append(t)
                next.append(list2[queue[i]][index])
    if len(next)==0:
        #print(record)
        print('No!',end='')
    else:
        #print(next)
        bfs(list2,target,next,re)

def main():
    n,x,y= map(int,input().split())
    list1 = dict()
    for i in range(n):
        x1,y1=map(int,input().split())
        if x1 not in list1:
            list1[x1]=list()
        if y1 not in list1:
            list1[y1]=list()
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