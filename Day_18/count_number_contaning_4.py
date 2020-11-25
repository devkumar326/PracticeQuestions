class Solution:
    def countNumberswith4(self, N):
        count=0
        for i in range(1,N+1):
            if(i<10):
                if(i==4):
                    count+=1
            elif(i>10):
                while(i>0):
                    s=i%10
                    if(s==4):
                        count+=1
                        i=0
                    i=i//10
        return count

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countNumberswith4(N))
