def decode(s):
    dp=[1]*(len(s)+1)
    if s[0]=="0":
        dp[1]=0
    for i in range(2,len(s)+1):
        dp[i]=(dp[i-1] if 1<=int(s[i-1])<=9 else 0)+(dp[i-2] if 10<=int(s[i-2]+s[i-1])<=26 else 0)
    return dp[-1]


for _ in range(int(input())):
    n=int(input())
    s=input()
    print(decode(s))