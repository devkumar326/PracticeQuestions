import atexit
import io
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''
def Dfs(g, i, visited, arr):
    arr.append(i)
    visited[i]=True
    for x in g[i]:
        if not visited[x]:
            Dfs(g, x, visited, arr)
def dfs(g,N):
    visited=[False]*N
    arr=[]
    Dfs(g, 0, visited, arr)
    return arr


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
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)

        res = dfs(g.graph,N)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()

