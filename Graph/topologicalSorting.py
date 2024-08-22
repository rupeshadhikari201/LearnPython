'''
Topological Sorting:
Linear ordering of vertices such that if there is an edge between u and v, u appears before v.

Application: 
1) Package managers like npm, pip, and apt use topological sorting to resolve dependencies, ensuring that a package is installed only after all its dependencies have been installed.
2) Compilers use topological sorting to determine the order of file compilation, especially in languages like C/C++ where certain files depend on others.
3) In version control, especially in systems like Git, topological sorting helps in resolving merge conflicts by determining the correct order of commits.
'''

'''

5     4
| \ / |
|  0  | 
2- 3 -1

Edges:
5->0
5->2
2->3
3->1
4->1
4->0

Topological ordering-I  : 5,4,2,3,1,0
Topological ordering-II : 4,5,2,3,1,0
'''

from typing import List


edges = [[5,0],[5,2],[2,3],[3,1],[4,1],[4,0]]
n = 6 # no of nodes

def createDirecteGraph(edges: List[List], n : int):
    # create a dict to store the adjacency matrix from the edges
    graph = {i:[] for i in range(n)}
    
    for edge in edges:
        u,v = edge
        graph[u].append(v)
    
    return graph

graph = createDirecteGraph(edges,n)

def dfs(i,graph,stack, visited):
    # mark i as visited
    visited[i] = True
    
    for neighbour in graph[i]:
        if visited[neighbour] == False:
            dfs(neighbour,graph,stack,visited)
    
    # add to the stack
    stack.append(i)
    

def topoSort(graph,n):
    visited = [False]*n
    stack = []
    print(visited)
    # for disconnected components
    for i in range(n):
        if visited[i] == False:
            dfs(i,graph,stack,visited)
            
    stack.reverse()
    print(stack)
    
topoSort(graph,n)


