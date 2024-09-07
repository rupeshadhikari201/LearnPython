from typing import List

n = 5 
k = 4 
mydict= ["baa","abcd","abca","cab","cad"]
nodes = []
for i in range(k):
    nodes.append(chr(97+i))
print(nodes)

def dfs(i,graph, visited,stack):
    # mark as visited
    visited[i] = True
    
    for neighbour in graph[nodes[i]]:
        index = ord(neighbour)
        if visited[index-97] == False:
            dfs(index-97,graph,visited,stack)

    # add to the stack
    stack.append(nodes[i])
        
    

def findOrder(mydict : List[str], n : int, k : int) -> str:
    # create a dict to store the adjacency matrix of DAG
    graph = {nodes[i]:[] for i in range(len(nodes))}
    edges = []
    for i in range(n-1):
        str1 = mydict[i]
        str2 = mydict[i+1]
        for i in range(min(len(str1),len(str2))):
            if str1[i] != str2[i]:
                edges.append([str1[i], str2[i]])
                break
    
    for edge in edges:
        u,v = edge
        graph[u].append(v)
    
    print(graph)
    # now lets do the topoligcal sort of this graph
    visited = [False] * k
    stack = []
    # for disconnected nodes
    for i in range(k):
        if visited[i] == False:
            dfs(i,graph,visited,stack)
    
    print(stack)
    stack.reverse()
    ordering = [''.join(i) for i in stack ]
    ordering = ''.join(i for i in stack)
    print(ordering)
        
findOrder(mydict,n,k)
    
    