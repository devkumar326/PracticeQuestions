class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i,j,k=0,0,0
        temp =[None]*n1
        ans=[]
        # Iterate through three arrays while all arrays have elements    
        while (i < n1 and j < n2 and k< n3): 
            # If x = y and y = z, print any of them and move ahead in all arrays
            if (A[i] == B[j] and B[j] == C[k]): 
                temp[i]=A[i]
                i += 1
                j += 1
                k += 1
                
            # x < y
            elif A[i] < B[j]: 
                i += 1
                
            # y < z     
            elif B[j] < C[k]: 
                j += 1
                
            # We reach here when x > y and z < y, i.e., z is smallest  
            else: 
                k += 1
        for i in temp:
            if i!=None and i not in ans:
                ans.append(i)
        return ans

t = int(input())
for tc in range (t):
    n1,n2,n3 = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ob = Solution()

    res = ob.commonElements(A,B,C,n1,n2,n3)

    if len(res)==0 :
        print(-1)
    else:
        for i in range (len(res)):
            print(res[i], end=' ')
        print()
