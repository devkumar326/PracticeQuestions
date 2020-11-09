class Solution:
    def countSquares(self, N):
        return int(math.sqrt(N-1))

import math

if __name__=='__main__':
    t=int(input())
    for _ in range (t):
        N=int(input())

        ob=Solution()
        print(ob.countSquares(N))