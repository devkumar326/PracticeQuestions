for _ in range(int(input())):
    n,m,k_req=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    i,j,k=0,0,0
    f=0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            k+=1
            if k==k_req:
                print(A[i])
                f=1
                break
            i+=1
        else:
            k+=1
            if k==k_req:
                print(B[j])
                f=1
                break
            j+=1
    if f==1:
        continue
    while i<len(A):
        k+=1
        
        if k==k_req:
                print(A[i])
                break
        i+=1
    while j<len(B):
        k+=1
        
        if k==k_req:
                print(B[j])
                break
        j+=1