from sys import stdin

res = ""
line = f"({input().strip()})"

for i, c in enumerate(line):
    if c == "[":
        res += "*("

    elif c == "]":
        res += ")+"

    elif c.isalpha():
        res += f"'{c}'+"
    else:
        res += c
print(res)
res = res.replace("+)", ")")

print(eval(res))
