def ispalin(st,pt1,pt2,left,right,lookup):
    while pt1>=left and pt2<right:
        if st[pt1]==st[pt2]:
            lookup.add(s[pt1:pt2+1])
            pt1-=1
            pt2+=1
        else:
            break
def distinctpalin(s):
    lookup=set()
    for i in range(len(s)):
        ispalin(s,i,i,0,len(s),lookup)
        ispalin(s,i,i+1,0,len(s),lookup)
    return len(lookup)

if __name__ == "__main__":
    t=int(input())
    while t>0:
        t=t-1
        s=input()
        print(distinctpalin(s))