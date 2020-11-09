import math
if __name__=="__main__":
    t=int(input())
    for _ in range (t):
        n=int(input())
        arr=list(map(int, input().strip().split(" ")))
        ans=1
        for x in arr:
            ans*=x
        for x in arr:
            if x!=0:
                print(ans//x, end=" ")
            else:
                print(ans, end=" ")
        print()