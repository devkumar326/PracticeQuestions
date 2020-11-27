
def maxArea(A,le):
    i=0
    j=len(A)-1
    result=0
    maxi=0
    for k in range(len(A)):
        if A[i]>A[j]:
            result=A[j]*(j-i)
            j-=1
        else:
            result=A[i]*(j-i)
            i+=1
        if maxi<result:
            maxi=result
    return maxi

for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
  