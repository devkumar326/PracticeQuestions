import sys
'''
*   g: vector of vectors which represents the graph
*   src: source vertex to start traversing graph with
*   V: number of vertices

'''
def dijkstra(src, V, g):
    '''
    :param g: adjacency matrix for graph
    :param src: source node
    :param V: number of nodes
    :return: print space separated shortest distance
    '''
    visited=[False for i in range(V)]
    dist=[sys.maxsize for i in range(V)]
    
    dist[src]=0
    
    for _ in range(V):
        
        u=mindistancenode(dist,visited)
        visited[u]=True
        
        for v in range(V):
            if g[u][v]>0 and visited[v]==False and dist[v]>dist[u]+g[u][v]:
                dist[v]=dist[u]+g[u][v]
                
    return dist
    
    
    
def mindistancenode(dist,visited):
    minu=sys.maxsize
    
    for i in range(len(dist)):
        if minu>dist[i] and visited[i]==False:
            minu=dist[i]
            min_index=i
    return min_index

def printSolution(dist, V):
    for node in range(V):
        print(dist[node] , end=" ")
    print()


if __name__ == '__main__':
    t = int(input())
    for tst in range(t):
        v = int(input())
        graph = [[0 for column in range(v)]
                    for row in range(v)]

        lst = [int(x) for x in input().strip().split()]
        k=0
        for i in range(v):
            for j in range(v):
                graph[i][j] = lst[k]
                k+=1
        s = int(input())
        res = dijkstra(s, v, graph)
        
        printSolution (res, v)
