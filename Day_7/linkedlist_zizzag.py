import io
import sys

def swap(head1, head2):
    temp=head1.data
    head1.data=head2.data
    head2.data=temp
    
def zigzag(head_node):
    ptr=head_node
    flip=True
    while ptr!=None and ptr.next!=None:
        if flip:
            if ptr.data>ptr.next.data:
                swap(ptr, ptr.next)
        else:
            if ptr.data<ptr.next.data:
                swap(ptr, ptr.next)
        flip= not flip
        ptr= ptr.next
    return head_node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        self.tail = self.tail.next

def print_list(head_node):
    curr_node = head_node
    while curr_node is not None:
        print(curr_node.data, end = ' ')
        curr_node = curr_node.next
    print()


if __name__ == '__main__':
    for cases in range(int(input())):
        n = int(input())
        nodes = list(map(int,input().strip().split()))
        a = LinkedList()
        for x in nodes:
            a.append(Node(x))
        
        print_list(zigzag(a.head))