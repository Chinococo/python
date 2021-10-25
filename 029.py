from functools import cmp_to_key


def key(i1,i2):
    if (i1^i2):
        return bool(i2&1)
    elif i1&1 and i2&1:
        return i1>i2
    else:
        return i2>i1

list1 = list(input().split())
for i in range(len(list1)):
    list1[i] = int(list1[i])
print(sorted(list1,key=cmp_to_key(key)))