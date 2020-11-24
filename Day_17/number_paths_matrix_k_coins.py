gdict = {}
def start_count(dp, i, j, goal, count, n):
    if count > goal or i >= n or j >= n:
        return 0
    if count == goal and (i, j) == (n-1, n-1):
        return 1
    else:
        if ((i,j),count) in gdict:
            return gdict[((i,j),count)]
        else:
            gdict[((i,j),count)] = start_count(dp, i, j+1, goal, count+dp[i][j], n) + start_count(dp, i+1, j, goal, count+dp[i][j], n)
    return gdict[((i,j),count)]
    
res = []
for _ in range(int(input())):
    goal = int(input())
    n = int(input())
    tnums = input().split(" ")
    nums = []
    for i in range(len(tnums)):
        if len(tnums[i]) > 0:
            nums.append(int(tnums[i]))
    
    dp = [[0 for i in range(n)] for j in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            dp[i][j] = nums[k]
            k+=1
    gdict = {}
    res.append(start_count(dp, 0, 0, goal, dp[0][0], n))
    
for xx in res:
    print(xx)
            
            
            
            
        
    