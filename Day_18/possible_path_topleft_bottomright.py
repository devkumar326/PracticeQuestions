
def get_ans(n, m):
    dp = [[0]*m for i in range(n)]
    for i in range(n):
        dp[i][-1] = 1
    for i in range(m):
        dp[-1][i] = 1
        
    for i in reversed(range(0, n-1)):
        for j in reversed(range(0, m-1)):
            dp[i][j] = (dp[i+1][j] + dp[i][j+1])%(pow(10,9)+7)
            
    return dp[0][0]
    
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, m = list(map(int, input().split()))
        print(get_ans(n, m))