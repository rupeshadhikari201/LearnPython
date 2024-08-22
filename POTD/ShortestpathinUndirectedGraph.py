from collections import deque

no_of_nodes = 9
no_of_edges = 10
src = 0
edges= [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 

def shortestPath(no_of_nodes,edges,src):
    
    # create the adjacency list representation of graph
    graph = {i:[] for i in range(no_of_nodes)}
    print(graph)
    
    for edge in edges:
        u,v = edge
        graph[u].append(v)
        graph[v].append(u) # For undirected graph
    print(graph)
    
    # initialize a distance array for size no_of_nodes
    distance = [-1] * no_of_nodes
    # distance from src node to itself is 0
    distance[src] = 0
    
    q = deque()
    q.append(src)
    
    while q:
        
        front = q.popleft()
        
        for neighbour in graph[front]:
            if distance[neighbour] == -1: # Not visited Neighbour
                distance[neighbour] = 1 + distance[front] 
                q.append(neighbour)
    return distance
    

print("The shortest path from {} to all other node is : ".format(src))
distance = shortestPath(no_of_nodes,edges,src)
print(distance)