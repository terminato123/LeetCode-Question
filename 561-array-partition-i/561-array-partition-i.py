class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s=0
        i=0
        while i<len(nums):
            s+=nums[i]
            i+=2
        return s
        