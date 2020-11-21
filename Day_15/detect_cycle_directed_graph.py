from collections import defaultdict

def dfs_visit(graph,n,s,t):
    s.add(n)
    t.add(n)
    book = False
    for v in graph[n]:
        if v in t:
            return True
        if v not in s:
            book = book or dfs_visit(graph,v,s,t)
    t.remove(n)
    return book

def isCyclic(n,graph):
    s = set()
    boo = False
    for i in range(n):
        if i not in s:
            t = set()
            boo = boo or dfs_visit(graph,i,s,t)
    return boo


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
