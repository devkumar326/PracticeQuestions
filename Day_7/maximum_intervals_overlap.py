for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    e=list(map(int,input().split()))
    ds={}
    de={}
    a=[]
    for i in s:
        if i in ds:
            ds[i]+=1
        else:
            ds[i]=1
            a.append(i)
    for i in e:
        if i in de:
            de[i]+=1
        else:
            de[i]=1
            if i not in ds:
                a.append(i)
    a.sort()
    c=0
    mx=0
    ix=-1
    for i in a:
        if i in ds:
            c+=ds[i]
        if c>mx:
            mx=c
            ix=i
        if i in de:
            c-=de[i]
    #print(a)  
    print(mx,ix)