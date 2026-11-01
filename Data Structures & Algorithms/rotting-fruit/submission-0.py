import numpy as np
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh_oranges,time = 0,0

        q = deque()

        ROWS,COLS = len(grid), len(grid[0])
        for r in range(0,ROWS):
            for c in range(0,COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1    
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        while q and fresh_oranges > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr, c+dc

                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    print(np.array(grid))
                    q.append([row,col])
                    fresh_oranges -= 1
            time += 1
        return time if fresh_oranges == 0 else -1
                