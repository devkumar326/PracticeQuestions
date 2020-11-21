import atexit
import io
import sys
from collections import defaultdict
import queue
from collections import deque
'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
def bfs(g,N):
    ret=[]
    q=deque()
    q.append(0)
    visited=[False]*N
    visited[0]=True
    while q:
        size=len(q)
        for i in range(size):
            curr=q.popleft()
            ret.append(curr)
            temp=g[curr]
            for x in temp:
                if not visited[x]:
                    visited[x]=True
                    q.append(x)
    return ret

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add a directed edge from u to v

        res = bfs(g.graph,N) # print bfs of graph
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
