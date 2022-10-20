class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        s=0
        if len(nums)<2:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            s=max(s,nums[i+1]-nums[i])
        return s
