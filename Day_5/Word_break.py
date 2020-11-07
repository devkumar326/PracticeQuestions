def wordbreak(s,i,lookup):
    if i==1:
        return True
    if s in lookup:
        return True
    ret=False
    for i in range(1,len(s)):
        if s[i:] in lookup:
            ret|=wordbreak(s[:i],i,lookup)
    return ret
t=int(input())
for _ in range(t):
    n=int(input())
    lookup=set(input().strip().split(" "))
    s=input()
    ans=wordbreak(s, len(s), lookup)
    if ans:
        print(1)
    else:
        print(0)