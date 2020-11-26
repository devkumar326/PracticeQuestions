def solve(i,j):
    if i >= x or j >= y:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] != s2[j]:
        dp[i][j] = max(solve(i+1,j),solve(i,j+1))
    else:
        count = 0
        tx = i
        ty = j
        while tx < x and ty < y and  s1[tx] == s2[ty]:
            count += 1
            tx += 1
            ty += 1
        dp[i][j] = max(count,max(solve(i+1,j),solve(i,j+1)))
    return dp[i][j]

for _ in range(int(input())):
    x, y = map(int,input().split())
    s1 = input()
    s2 = input()
    dp = [[-1 for x in range(len(s2) + 1)] for y in range(len(s1) + 1) ]
    print(solve(0,0))