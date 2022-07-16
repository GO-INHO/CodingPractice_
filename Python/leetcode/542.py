class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])
        row_len = len(mat)
        col_len = len(mat[0])
        for i in range(row_len):
            for j in range(col_len):
                if mat[i][j] == 0:
                    q.append([i, j, 0])
                else:
                    mat[i][j] = math.inf
        
        while( len(q) ):
            i , j , dist = q.popleft()
            dir = [[0,1],[0,-1],[1,0],[-1,0]]
            if mat[i][j] > dist:
                mat[i][j] = dist
            for x, y in dir:
                new_x = i + x
                new_y = j + y
                if new_x >= 0 and new_y >= 0 and new_x < row_len and new_y < col_len:
                    if mat[new_x][new_y] == math.inf:
                        q.append([new_x, new_y, dist + 1])
                        
        return mat
    
    
                    
            
            
'''

I: 2차원 리스트
O: 2차원 리스트
C: 
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

E:
ds: 
algo: 

solution: dfs 돌면서 0이 나오는 깊이까지 탐색

N : 
time:  
space: 
'''