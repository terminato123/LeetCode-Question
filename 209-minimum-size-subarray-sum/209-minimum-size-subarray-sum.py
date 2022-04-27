class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        res=float("inf")
        for i in range(len(nums)):
            r+=nums[i]
            while r>=target:
                res=min(i-l+1,res)
                r-=nums[l]
                l+=1
        return 0 if res==float("inf") else res
        