import io
import sys
import heapq
from collections import  defaultdict
def minCost(a,n) :
    '''
    use heapq module , imported already by driver code.
    :param a: given array
    :param n: size of array
    :return: Integer
    '''
    heap=[]
    for i in a:
        heapq.heappush(heap,i)
    
    c,m=0,0
    while n>1:
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        m=a+b
        c=c+m
        heapq.heappush(heap,m)
        n-=1
        
    return c

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(minCost(a,n))