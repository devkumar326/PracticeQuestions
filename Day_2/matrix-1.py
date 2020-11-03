t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    mat = []
    for i in range(0,n*n,n):
        mat.append(arr[i:i+n])
        
    for i in range(n):
        for j in range(n):
            print(mat[j][n-1-i],end=" ")
    print()

