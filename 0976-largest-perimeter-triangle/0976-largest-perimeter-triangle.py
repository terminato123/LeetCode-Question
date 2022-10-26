class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        lenght=len(nums)
        i=lenght-1
        nums.sort()
        while i>=2:
            if (nums[i-2]+nums[i-1])>nums[i]:
                return (nums[i-2]+nums[i-1]+nums[i])
            i-=1
        return 0
        