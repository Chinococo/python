def isValid( s: str) :
    set1 = {'(', '{', '['}
    dict1 = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    list1 = []
    for i in range(len(s)):
        if (len(list1) == 0 or s[i] in set1):
            list1.append(s[i])
        elif (dict1[s[i]] == list1[len(list1) - 1]):
            list1.pop()
        else:
            return False
    return bool(len(list1) == 0)
print(isValid('()[]{}'))