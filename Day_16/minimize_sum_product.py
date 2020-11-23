t=int(input(""))
for i in range(t):
    n=int(input(""))
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    d=sorted(b,reverse=True)
    sum=0
    for i in range(n):
        sum+=a[i]*d[i]
    print(sum)