for i in range (int(input())):
    n=int(input())
    arr=sorted(list(map(int, input().split())))
    m=int(input())
    ans=10000000000000000000
    for x in range(0,n-m+1):
        if arr[x+m-1]-arr[x] < ans:
            ans = arr[x+m-1] - arr[x]
        if ans ==0:
            break
    print(ans)