"""
0 -- 1 -- 4
|    |
2 -- 3

BFS Traversal : 0,1,2,4,3
"""

def dfs(graph,node,visited=None):
    if visited is None:
        visited = set()
        
    visited.add(node)
    print(node, end=' ')
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour,visited)

# Adjacency List
graph = {
    0 : [1,2],
    1 : [0,3,4],
    2 : [0,3],
    3 : [1,2],
    4 : [1]
}

print("The Dfs Traversal is : ")
start_node = 0
dfs(graph,start_node)