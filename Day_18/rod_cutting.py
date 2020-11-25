def rodcutting(val, n, i, dp):
    if i>len(val):
        return 0
    if n<0:
        return 0
    if dp[i][n]!=-1:
        return dp[i][n]
    temp=n-i-1
    smallans1=0
    smallans2=0
    if temp>=0:
        smallans1=val[i]+rodcutting(val, temp, i, dp)
    smallans2=rodcutting(val, n, i+1, dp)
    dp[i][n]=max(smallans1, smallans2)
    return dp[i][n]
    
if __name__=='__main__':
    t=int(input())
    while t>0:
        t=t-1
        n=int(input())
        arr=list(map(int, input().strip().split(" ")))
        dp=[[-1]*(n+1) for x in range(n+1)]
        print(rodcutting(arr, n, 0, dp))