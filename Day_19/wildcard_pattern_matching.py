def matching(pattern, st, i, j, dp):
    if i==-1 and j==-1:
        return True
    if pattern[0]=="*" and j==-1:
        return True
    if i==-1 or j==-1:
        return False
    if dp[i][j]!=-1:
        return dp[i][j]
    if pattern[i]=="?":
        dp[i][j]=matching(pattern, st, i-1, j-1, dp)
    elif pattern[i]=="*":
        ans1=matching(pattern, st, i, j-1, dp)
        ans2=matching(pattern, st, i-1, j-1, dp)
        ans3=matching(pattern, st, i-1, j, dp)
        dp[i][j]=ans1 or ans2 or ans3
    elif pattern[i]==st[j]:
        dp[i][j]=matching(pattern, st, i-1, j-1, dp)
    else:
        dp[i][j]=False
    return dp[i][j]

def wildCard(str1, str2):
    dp=[[-1]*len(str1) for x in range(len(str2))]
    return matching(str2, str1, len(str2)-1, len(str1)-1, dp)

t = int(input())
for i in range(t):
    str1 = input().strip()
    str2 = input().strip()
    if wildCard(str2, str1):
        print(1)
    else:
        print(0)