'''
node class:
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
import heapq
def mergeKLists(arr,N):
    save = []
    for i in range(n):
        queue = heads[i]
        while queue:
            heapq.heappush(save, queue.data)
            queue = queue.next
            
    new_head = Node(heapq.heappop(save))
    temp = new_head
    
    for _ in range(len(save)):
        temp.next = Node(heapq.heappop(save))
        temp = temp.next
    return new_head

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = mergeKLists(heads,n)
        printList(merged_list)
