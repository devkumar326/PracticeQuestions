class Solution:
    def heaping(self,arr,n):
        for i in range((n-1)//2,-1,-1):
            self.heapify(arr,i)
    def heapify(self,arr,i):
        if i<len(arr):
            left=2*i+1
            right=2*i+2
            maxval=i
            if left<len(arr) and arr[left]>arr[maxval]:
                maxval=left
            if right<len(arr) and arr[right]>arr[maxval]:
                maxval=right
            if maxval!=i:
                temp=arr[maxval]
                arr[maxval]=arr[i]
                arr[i]=temp
                self.heapify(arr,maxval)
    def pop(self,arr):
        if len(arr)>0:
            ret=arr[0]
            arr[0]=arr.pop()
            self.heapify(arr,0)
            return ret
    def kLargest(self,arr, n, k):
        self.heaping(arr,n)
        ret=[]
        while k>0:
           k-=1
           ret.append(self.pop(arr))
        return ret

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1