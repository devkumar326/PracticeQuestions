def floodFill(screen, x, y, prevC, newC, N, M):
    if (x < 0 or x >= M or y < 0 or 
        y >= N or screen[x][y] != prevC or 
        screen[x][y] == newC): 
        return
    screen[x][y] = newC 
    floodFill(screen, x + 1, y, prevC, newC, N, M) 
    floodFill(screen, x - 1, y, prevC, newC, N, M) 
    floodFill(screen, x, y + 1, prevC, newC, N, M) 
    floodFill(screen, x, y - 1, prevC, newC, N, M) 

for i in range(int(input())):
    M,N = [int(_) for _ in input().split()]
    Arr = [int(_) for _ in input().split()]
    X,Y,K = [int(_) for _ in input().split()]
    screen = []
    for i in range(M):
        screen.append(Arr[i*N:i*N+N])
    prevC = screen[X][Y]
    floodFill(screen, X, Y,prevC,  K, N, M)
    for item in screen:
        print(*item, end=' ')
    print(' ')