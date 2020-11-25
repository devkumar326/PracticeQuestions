class Nqueen(object):
    def __init__(self):
        self.count = 0
        
    def isSafe(self, mat, row, col, n):
        curR = row
        curC = col
        while curR >= 0: #check in the part of row above
            if mat[curR][curC] == 1:
                return False
            curR -= 1
        
        curR = row
        curC = col
        while curC >= 0: # check the upper diagonal on the left side
            if mat[curR][curC] == 1:
                return False
            curR -= 1
            curC -= 1
            
        curR = row
        curC = col
        while curC < n and curR >= 0: # check the upper diagonal on the right side
            if mat[curR][curC] == 1:
                return False
            curR -= 1
            curC += 1  
        return True
        
    def findComb(self, mat, n, arr, curRow):
        if curRow == n:
            print('[' + ' '.join(arr) + ' ]', end = ' ') 
            self.count += 1
            return

        for j in range(n):
            if self.isSafe(mat, curRow, j, n):
                mat[curRow][j] = 1
                arr.append(str(j + 1))
                self.findComb(mat, n, arr, curRow + 1)
                arr.pop()
                mat[curRow][j] = 0
        
    def Tcount(self):
        return self.count
        
for _ in range(int(input())):
    n = int(input())
    mat = [[0 for i in range(n)] for j in range(n)]
    q = Nqueen()
    q.findComb(mat, n, [], 0)
    count = q.Tcount()
    if count == 0:
        print(-1, end = ' ')
    print()
    