def main():
    dp = [[0 for i in range(11)] for x in range(100002)]
    dp[1][0]=9
    for i in range(9,0,-1):
        dp[1][i] = (9-i+1)
    for x in range(2,100002):
        for y in range(9,-1,-1):
            for in0dex in range(y,10):
                dp[x][y] += dp[x-1][index]
    #for x in range(0,100):
            #print((dp[x]))

    s = input()
    ans = 0
    prev = 0
    for i in range(len(s)):
        for index in range(prev,int(10)):
            print(dp[len(s)-i-1][index])
            ans+=dp[len(s)-i-1][index]

        if prev>int(s[i]):
            break
        prev = int(s[i])
    print(ans)
main()