class Solution:
    def numDecodings(self, s: str) -> int:
        v=[str(i) for i in range(1,27)]
        k=len(s)
        dp=[0]*(k+1)
        dp[0]=1
        for i in range(1,k+1):
            if s[i-1] in v:
                dp[i]+=dp[i-1]
            if i>1 and s[i-2:i] in v:
                dp[i]+=dp[i-2]
        return dp[-1]
        