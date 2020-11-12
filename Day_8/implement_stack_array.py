class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Adds element to the Stack
    def push(self,data):
        self.arr.append(data)
    
    #Removes element from the stack
    def pop(self):
        if(len(self.arr)==0):
            return -1
        
        return self.arr.pop()

t=int(input())
for i in range(t):
    s=MyStack()
    q=int(input())
    q1=list(map(int,input().split()))
    i=0
    while(i<len(q1)):
        if(q1[i]==1):
            s.push(q1[i+1])
            i=i+2
        elif(q1[i]==2):
            print(s.pop(),end=" ")
            i=i+1
        elif(s.isEmpty()):
            print(-1)
            i=i+1
    print()