class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        if len(nums)==0:
            return 0
        i=0
        def fact(nums,i,dp):
            
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            else:
                r=max(nums[i]+fact(nums,i+2,dp),fact(nums,i+1,dp))
                dp[i]=r
            return dp[i]
        return fact(nums,i,dp)
