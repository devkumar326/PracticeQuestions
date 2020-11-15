import io
import sys
'''
Function Arguments :
		@param  : queue ( given queue to be used), k(Integer ),n(size of queue)
		@return : lsit, just reverse the first k elements of queue and return new queue
'''

def reverseK(queue,k,n):
    front=queue[:k]
    back=queue[k:]
    front=front[::-1]
    queue=front+back
    return queue

if __name__=='__main__':
    testcases= int(input())
    for cases in range (testcases):
        n,k= map(int, input().strip().split())
        a= list(map(int, input().strip().split()))

        queue=[]
        for i in range(n):
            queue.append(a[i])

        print(*reverseK(queue,k,n))