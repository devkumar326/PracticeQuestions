class Solution:

    def numberOfPaths (self, m, n):
        m-=1
        n-=1
        ans=1
        for x in range (1, m+1, 1):
            ans=(ans*(n+x))//x
        return ans

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)
