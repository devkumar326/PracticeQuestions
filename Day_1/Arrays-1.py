for i in range (int(input())):
    n,m=(int(i) for i in input().split())
    a=list(map(int, input().strip().split()))
    b=list(map(int, input().strip().split()))
    s=set(a+b)
    print(len(s))