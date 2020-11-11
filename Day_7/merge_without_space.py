
class Solution:
    def merge(self, arr1, arr2, n, m): 
        arr1.extend(arr2)
        arr1.sort()
        for i in range(1, m+1):
            arr2[-i]=arr1.pop()

tc=int(input())
while tc> 0:
    n,m=map(int, (input().strip().split()))
    arr1=list(map(int, input().strip().split()))
    arr2=list(map(int, input().strip().split()))
    ob= Solution()
    ans= ob.merge(arr1, arr2, n, m)
    for x in arr1:
        print(x, end=" ")
    for x in arr2:
        print(x, end=" ")
    print()
    tc-=1