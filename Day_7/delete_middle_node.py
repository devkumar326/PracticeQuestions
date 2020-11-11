def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    sptr=head
    fptr=head
    prev=None
    while fptr!=None and fptr.next!= None:
        fptr=fptr.next.next
        prev=sptr
        sptr=sptr.next
    temp=sptr
    prev.next=sptr.next
    temp.next=None
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)

        res=deleteMid(ll.head)
        printList(res)