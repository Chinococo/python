str1 = input()
l = len(str1)
dp = [[False for i in range(l)]for x in range(l)]
for i in range(l):
    dp[i][i] = True
for i in range(l-1):
    dp[i][i+1] = str1[i]==str1[i+1]
for y in range(l):
    for x in range(y-2,-1,-1):
        dp[x][y] = dp[x+1][y-1] and  str1[x]==str1[y]
ans = set()

for x in range(l):
    for y in range(x,l):
        if dp[x][y]:
           ans.add(str1[x:y+1])

print('#'.join(sorted(ans)))