if __name__ == '__main__':
    dp=[1]*1001
    for i in range(1,1001):
        dp[i]=i*dp[i-1]
    for _ in range(int(input())) :
        n = int(input())
        print(dp[n])