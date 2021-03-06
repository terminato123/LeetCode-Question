class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for i in range(n)]
        # dp = grid[:]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    
                
                    
                    dp[i][j] = min(grid[i][j] + dp[i - 1][j], grid[i][j] + dp[i][j - 1])
        return dp[-1][-1] 
            
            
        