#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum1):
	    dp=[[0]*(sum1+1) for i in range(n+1)]
	    dp[0][0]=1
	    for i in range(1,sum1+1):
	        dp[0][i]=0
	    for i in range(1,n+1):
	        for j in range(sum1+1):
	           if arr[i-1]<=j:
	               dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
	           else:
	               dp[i][j]=dp[i-1][j]
	    return (dp[n][sum1])%(10**9+7)
		# code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends