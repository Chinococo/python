dict1 = {}
for i in range(3):
    no = input()
    hour = int(input())
    for k in range(hour):
        t = input()
        if(t in dict1.keys()):
            print('{} and {} confict on {}'.format(dict1[t],no,t))
        else:
            dict1[t] = no


