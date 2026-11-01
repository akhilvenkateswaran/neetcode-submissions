import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: 

        row,col = len(grid), len(grid[0])
        res = 0
        directions = [[-1,0],[0,1],[1,0],[0,-1]]

        def dfs(r,c):

            if (r < 0 or c < 0 or r>=row or c>=col or grid[r][c] == "0" or grid[r][c] == "V"):
                return
            
            grid[r][c] = "V"
            print(np.array(grid))
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
                    print('Printing after return',res)
        return res



        