class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t=len(text1)
        t1=len(text2)
        dp=[[-1]*(t1+1) for i in range(t+1)]
        def lcs(s1,s2,n,m,dp):
            if n==0 or m==0:
                return 0
            if dp[n][m]!=-1:
                return dp[n][m]
            if (s1[n-1]==s2[m-1]):
                dp[n][m]=lcs(s1,s2,n-1,m-1,dp)+1
                return dp[n][m]
            dp[n][m]=max(lcs(s1,s2,n-1,m,dp),lcs(s1,s2,n,m-1,dp))
            return dp[n][m]
        return lcs(text1,text2,t,t1,dp)
         