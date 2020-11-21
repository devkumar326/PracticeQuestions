class Solution:
    def minStep (self, n):
        count = 0
        while (n > 1):
            if (n%3 == 0):
                count+=1
                n = n/3
            else:
                count+=1
                n = n-1
        return count

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minStep(n))
