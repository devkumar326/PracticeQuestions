
import io
import sys
from collections import  defaultdict
'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''
def buildtree(dct,pos,ins,ine,ps,pe):
    if ins<=ine:
        root=Node(pos[pe])
        temp=dct[pos[pe]]
        root.left=buildtree(dct, pos, ins, temp-1, ps, temp-ins-ps-1)
        root.right=buildtree(dct, pos, temp+1, ine, ine-temp-pe, pe-1)
        return root
    else:
        return None

def buildTree(In, post, n):
    dct={}
    for i in range(0,len(In)):
        dct[In[i]]=i
    return buildtree(dct, post, 0, len(In)-1, 0, len(post)-1)
    
    '''
    :param In: given in order array
    :param post: given post order array
    :param n: number of nodes in tree
    :return: root of the created tree 
    '''


# Helper function that allocates  
# a new node  
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# This funtcion is here just to test  
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        in_order = list(map(int, input().strip().split()))  # parent child info in list
        post_order = list(map(int, input().strip().split()))  # parent child info in list
        preOrder(buildTree(in_order,post_order,n))
        print()