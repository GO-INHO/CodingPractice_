class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_num = len(image)
        col_num = len(image[0])
        print(row_num)
        print(col_num)
        exist_color = image[sr][sc]
        new_color = color
        def dfs(sr, sc):
            if sr < 0 or sr >= row_num or sc < 0 or sc >= col_num:
                return
            if image[sr][sc] == new_color:
                return
            if image[sr][sc] != exist_color:
                return
            
            image[sr][sc] = new_color
            
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)

        dfs(sr, sc)
        return image
        
        '''
        
I: 2차원 배열
O: 2차원 배열
C:
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n

E:


ds: 
algo: 

solution: 


N : 배열의 크기
time:  O(N)
space: O(N)
        
        '''