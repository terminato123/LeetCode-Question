class Solution:
    def uniquePathsWithObstacles(self, nums: List[List[int]]) -> int:
        if nums[0][0] == 1:
            return 0
        dp = [[0]*len(nums[0]) for j in range(len(nums))]
                                                
        #dp[0][0] = 1-nums[0][0]
        dp[0][0] = 1
        for i in range(1 , len(nums[0])):
            if nums[0][i] == 1:
                break
            else:
                #print('ya')
                dp[0][i] = 1
        
        for i in range(1 , len(nums)):
            if nums[i][0] == 1:
                break
            else:
                #print('sa' , i , 0)
                dp[i][0] = 1
           
        
        for i in range(1 , len(nums)):
            for j in range(1 , len(nums[0])):
                if nums[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        #print(dp)
        return dp[-1][-1]
                
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n=len(obstacleGrid)
#         m=len(obstacleGrid[0])
#         sr=set()
#         sc=set()
#         if obstacleGrid[0][0]==1:
#             return 0
        
#         for i in range(n):
#             for j in range(m):
#                 if obstacleGrid[i][j]==1:
#                     sr.add(i)
#                     sc.add(j)
                    
#         for i in range(n):
#             for j in range(m):
                
#                 if i in sr and j in sc:
#                     obstacleGrid[i][j]=0
                
#                 else:
#                     obstacleGrid[i][j]=1
                    
#         # for i in range(1,n):
#         #     for j in range(1,m):
#         #         if obstacleGrid[i][j]==0:
#         #             continue
#         #         obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                
#         print(obstacleGrid)
#         return obstacleGrid[-1][-1]
        