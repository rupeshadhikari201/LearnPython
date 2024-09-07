from collections import deque

def bfs_2d_matrix(grid):
    # if not matrix will check if the matrix is empty or not defined
    # In Python, an empty list is considered False when evaluated in a boolean context. So, not matrix will be True
    if not grid or not grid[0]:
        return []

    row_len = len(grid)
    col_len = len(grid[0])
    
    # visited array
    visited  = [[False for _ in range(col_len)] for _ in range(row_len)]
    
    # directions (right, down, left, up)
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    # start bfs from top corner
    q = deque([(0,0)])
    visited[0][0] = True
    traversal_order = []
    
    while q:
        pass
    

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix1 = [[]]
matrix2 = [[],[1,32]]
if not matrix1:
    print("empty")
else:
    print("non empty")
bfs_2d_matrix(matrix)