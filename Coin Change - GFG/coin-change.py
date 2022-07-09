#User function Template for python3

class Solution:
    def count(self, S, m, n): 
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
                    
        # code here 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends