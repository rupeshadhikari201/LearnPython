"""
0 -- 1 -- 4
|    |
2 -- 3

BFS Traversal : 0,1,2,4,3
"""

from collections import deque

def bfs(graph,node):
    # set to track visited node
    s = set()
    q = deque()
    q.append(node)
    s.add(node)
    
    while q:
        
        front = q.popleft()
        print(front, end=' ')
        
        # check for neighbours in front
        for neighbour in graph[front]:
            if neighbour not in s:  
                q.append(neighbour)
                s.add(neighbour)

# Adjacency List
graph = {
    0 : [1,2],
    1 : [0,3,4],
    2 : [0,3],
    3 : [1,2],
    4 : [1]
}

print('The Bfs Traversal is : ')
bfs(graph,0)


        
        


