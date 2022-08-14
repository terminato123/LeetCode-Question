class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        left=0
        for i in range(len(nums)):
            left+=nums[i]
            if t-left==left-nums[i]:
                return i
        return -1
        