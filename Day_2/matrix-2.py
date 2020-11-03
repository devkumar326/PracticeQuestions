for x in range(int(input())):
    a,b=list(map(int,input().split()))
    l=list(map(int,input().split()))
    matrix=[[0]*b for i in range(a)]
    t=0
    for i in range(a):
        for j in range(b):
            matrix[i][j]=l[t]
            t+=1
    top=0
    bottom=len(matrix)-1
    left=0
    right=len(matrix[0])-1
    dir1=0
    a=[]
    while top<=bottom and left<=right:
        if dir1==0:
            for i in range(left,right+1):
                print(matrix[top][i],end=" ")
            top+=1
        elif dir1==1:
            for i in range(top,bottom+1):
                print(matrix[i][right],end=" ")
            right-=1
        elif dir1==2:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
            bottom-=1
        elif dir1==3:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=" ")
            left+=1
        dir1=(dir1+1)%4    
    print("")    
            
    