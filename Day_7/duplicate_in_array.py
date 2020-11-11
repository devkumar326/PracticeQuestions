def duplicates(arr, n):
    dict1={}
    for x in arr:
        if x in dict1:
            dict1[x]+=1
        else:
            dict1[x]=1
    ret=[]
    for x in dict1:
        if dict1[x]>1:
            ret.append(x)
    if ret:
        ret.sort()
        return ret
    else:
        return [-1]
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split()))
    res= duplicates(arr, n)
    for i in res:
        print(i, end=" ")
    print()