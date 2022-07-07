class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        s=sum(nums)//2
        n=len(nums)
        dp = [[-1]*(s+1) for i in range(len(nums)+1)]
        
        def f(s,nums,n):
            k=str
            if n==0:
                return False
            if s==0:
                return True
            if dp[n][s] != -1:
                return dp[n][s]
            if nums[n-1]<=s:
                dp[n][s] =  f(s-nums[n-1],nums,n-1) or f(s,nums,n-1)
                return dp[n][s]
            dp[n][s] = f(s,nums,n-1)
            return dp[n][s]
        return f(s,nums,n)
            
        