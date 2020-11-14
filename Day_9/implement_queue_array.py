class MyQueue:
    def __init__(self):
        self.queue = list()
        self.maxSize = 100005
        self.head = 0
        self.tail = 0

    def push(self,data):
        if self.size() >= self.maxSize:
            return ("Queue Full")
        self.queue.append(data)
        self.tail += 1
        return      

    def pop(self):
        if self.size() <= 0:
            self.resetQueue()
            return -1 
        data = self.queue[self.head]
        self.head+=1
        return data
                
    def size(self):
        return self.tail - self.head
    
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
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