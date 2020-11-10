class Solution:
    def countBits(self, a):
        count = 0
        while (a):
            if (a & 1 ):
                count += 1
            a = a>>1
        return count
        
    def sortBySetBitCount(self, arr, n):
        count = [[] for i in range(32)]
        setbitcount = 0
        for i in range(n):
            setbitcount = self.countBits(arr[i])
            count[setbitcount].append(arr[i])
        j = 0
        for i in range (31,-1, -1):
            v1 = count[i]
            for i in range(len(v1)):
                arr[j] = v1[i]
                j += 1

T=int(input())
while(T>0):
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ob=Solution()
    ob.sortBySetBitCount(arr, n)
    print(*arr)
    T-=1