class Solution:
    def change(self, n: int, S: List[int]) -> int:
        m=len(S)
        dp=[[0]*(m+1) for i in range(n+1)]
        dp[0][0]=1
        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j]=dp[i][j-1]
                if S[j-1]<=i:
                    dp[i][j]+=dp[i-S[j-1]][j]
        return dp[n][m]
        
        