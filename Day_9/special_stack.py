# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    if (len(arr)==0):
        return int("-1")
    return arr.pop()

# function should return 1/0 or True/False
def isFull(n, arr):
    if (len(arr)==n):
        return True
    return False
        
# function should return 1/0 or True/False
def isEmpty(arr):
    if arr.top == None:
        return True
    else:
        return False

# function should return minimum element from the stack
def getMin(n, arr):
    if (len(arr)==0):
        return int("-1")
    return min(arr)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    stack = []
    for i in range(n):
        push(stack, arr[i])
    print(getMin(n, stack))