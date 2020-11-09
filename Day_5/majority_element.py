def findCandidate(A):
    maj_index=0
    count=1
    for i in range (len(A)):
        if(A[maj_index]==A[i]):
            count+=1
        else:
            count-=1
        if (count==0):
            maj_index=i
            count=1
    return A[maj_index]
    
def isMajority(A,cand):
    count=0
    for i in range (len(A)):
        if (A[i]==cand):
            count+=1
    if (count>len(A)/2):
        return True
    else:
        return False
            
def printMajority(A):
    cand=findCandidate(A)
    if(isMajority(A,cand)==True):
        print(cand)
    else:
        print(-1)
T=int(input())
while(T>0):
    n=int(input())
    A=[int(i) for i in input().split()]
    printMajority(A)
    T-=1
                