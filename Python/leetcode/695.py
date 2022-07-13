class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_num = len(grid)
        col_num = len(grid[0])
        
        max_num = 0
        dfs_num = 0
        visited = deepcopy(grid)
        
        ##########################################################################
        
        def dfs(i, j, num): # 반환값 : 넓이의 합.
            if i < 0 or i >= row_num or j < 0 or j >= col_num:
                return 0
            if grid[i][j] == 0:
                return 0
            if visited[i][j] == 0:
                return 0
            
            area = 1 #한칸의 넓이
            
            visited[i][j] = 0
            
            area += dfs(i+1, j, num + 1)
            area += dfs(i-1, j, num + 1)
            area += dfs(i, j+1, num + 1)
            area += dfs(i, j-1, num + 1)
            
            return area
            
       #############################################################################
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == 1 and visited[i][j] == 1:
                    max_num = max(max_num, dfs(i, j, 1))
                    
        return max_num
    
    
    
    
    '''
    top_down:
    재귀{
    return dfs...
    글로벌변수..
    
    }
    바텀업
    '''