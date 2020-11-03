def findLongestSubseq(arr,n):
    s=set()
    ans=0
    for ele in arr:
        s.add(ele)
    for i in range(n):
        if(arr[i]-1) not in s:
            j=arr[i]
            while (j in s):
                j+=1
            ans=max(ans,j-arr[i])
    return ans
T=int(input())
while(T>0):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(findLongestSubseq(arr,n))
    T-=1