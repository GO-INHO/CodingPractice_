class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        row_len = len(grid)
        col_len = len(grid[0])
        num_1 = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
                if grid[i][j] == 1:
                    num_1 += 1
        
        
        max_num = 0
        while( len(q) ):
            i , j , dist = q.popleft()
            dir = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for x, y in dir:
                new_x = i + x
                new_y = j + y
                if new_x >= 0 and new_y >= 0 and new_x < row_len and new_y < col_len:
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        num_1 -= 1
                        q.append([new_x, new_y, dist + 1])
                        max_num = max(max_num, dist + 1)
        
        if num_1 >= 1: return -1
        else: return max_num
        
'''

I: 2차원 리스트
O: 정수형 ()
C:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
E:


ds: 
algo: bfs

solution:
q = i ,j , 0
2(썩은 오렌지) q 
인접한 애들을 q에서 빼가지고
인접 검사 하면서 만약에 1이 있으면, 얘들을 넣어주면서


신선한 오렌지의 갯수 > 1 이상인데 bfs-> output -> -1


N : 
time:  
space: 
'''
        