def dfs(A, B, C, i, j, n):
    if n == len(C):
        return True
    ret = False
    if i < len(A) and A[i] == C[i+j]:
        ret = ret or dfs(A, B, C, i+1, j, n+1)
    if j < len(B) and B[j] == C[i+j]:
        ret = ret or dfs(A, B, C, i, j+1, n+1)
    return ret

def isInterleave(A, B, C):
    return dfs(A, B, C, 0, 0, 0)


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)