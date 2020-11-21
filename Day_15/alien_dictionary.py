'''
dict : array of strings denoting the words in alien langauge
N : Size of the dictionary
K : Number of characters
'''
def dfs(graph, visited, u, result):
    visited[u] = True
    
    for j in graph.get(u, []):
        if visited[j] is False:
            dfs(graph, visited, j, result)
    result.append(u)

def findOrder(alien_dict,n,k):
    graph = {}
    visited = {}
    alpha = []
    
    for i in range(1, len(alien_dict)):
        for j in range(min(len(alien_dict[i-1]), len(alien_dict[i]))):
            if alien_dict[i-1][j] != alien_dict[i][j]:
                graph.setdefault(alien_dict[i-1][j], [])
                graph[alien_dict[i-1][j]].append(alien_dict[i][j])
                break
    
    for word in alien_dict:
        for letter in word:
            if letter not in visited:
                visited[letter] = False
                # Alpha is used here to preserve order of letters.
                # Ordered dict can also be used for visited.
                alpha.append(letter)
    
    result = []
    for i in alpha:
        if visited[i] is False:
            dfs(graph, visited, i, result)
    result.reverse()
    return result


class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        
        order = findOrder(alien_dict,n,k)
        
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)
        
        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)
