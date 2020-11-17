'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def Dist(root, n, val = 0):
    temp = 0
    if root.data == n:
        return val
    if root.left:
        temp+=Dist(root.left, n, val+1)
    if root.right:
        temp+=Dist(root.right, n, val+1)
    if root.left is None and root.right is None:
        return 0
    return temp

def LCA(root, n1, n2):
    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root
        
    temp1 = LCA(root.left, n1, n2)
    temp2 = LCA(root.right, n1, n2)
    
    if temp1 and temp2:
        return root
    if temp1:
        return temp1
    else:
        return temp2

def findDist(root,a,b):
    #return: minimum distance between a and b in a tree with given root
    n1 = Dist(root, a)
    n2 = Dist(root, b)
    c = LCA(root, a, b)
    n3 = Dist(root, c.data)
    #print(n1, n2, n3)
    return n1 + n2 - 2*n3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        print(findDist(root, a, b))
