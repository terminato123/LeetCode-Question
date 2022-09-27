class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_1=sum(nums)
        var=0
        for i in nums:
            var+=i
            if var>max_1:
                max_1=var
            if var<0:
                var=0
        return max_1
        