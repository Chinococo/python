def count(s):
    c = 0
    for i in range(len(s)):
        if s[i].islower():
            c += 1
        elif s[i].isupper():
            c += 2
        elif s[i].isdigit():
            c += 3
        else:
            c += 5
    for i in range(len(s) - 5):
        if s[i] == s[i + 2] == s[i + 4] and s[i + 1] == s[i + 3]:
            c += 10
            break

    return c


mi = 100000
strmi = ''
ma = -1
strma = ''

while True:
    line = input()
    if (line == '-1'):
        break
    if mi > count(line):
        mi = count(line)
        strmi = line
    if ma < count(line):
        ma = count(line)
        strma = line

print(strma, ma)
print(strmi, mi)
