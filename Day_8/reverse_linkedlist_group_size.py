def reverse(head, k):
    start=head
    temp=None
    prev=None
    next=None
    cur=head
    i=0
    c=0
    while cur is not None:
        temp= cur
        prev= None
        while cur is not None and i<k:
            i+=1
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        if c==0:
            head=prev
        else:
            start.next=prev
            start=temp
        c+=1
        i=0
    return head

class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1