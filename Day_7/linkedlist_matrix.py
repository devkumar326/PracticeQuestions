def construct(arr, n):
    result = [[0]*len(arr[0]) for i in range(len(arr))]
    for i in range(n):
        for j in range(n):
            temp = Node(arr[i][j])
            result[i][j] = temp
    for i in range(n):
        for j in range(n):
            if j+1<n: 
                result[i][j].right=result[i][j+1]
            if i+1<n:
                result[i][j].down=result[i+1][j]
    return result[0][0]

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        Dp=self.head
        while (Dp):
            Rp = Dp
            while (Rp):
                print(Rp.data, end=" ")
                Rp = Rp.right
            Dp=Dp.down
        print("")

if __name__=='__main__':
    t = int(input())
    while(t>0):
        n = int(input())
        arr = [[0 for i in range(n)] for j in range(n)]
        listto = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range(n):
                arr[i][j] = listto[k]
                k=k+1

        llist = LinkedList()
        llist.head = construct(arr, n)
        llist.display()
        t=t-1