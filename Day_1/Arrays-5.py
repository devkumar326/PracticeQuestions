T=int(input())
while(T>0):
    n=int(input())
    arr=[int(x) for x in input().split()]
    k=int(input())
    arr.sort()
    print(arr[k-1])
    T-=1