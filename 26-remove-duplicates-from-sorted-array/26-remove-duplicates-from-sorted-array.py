class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        while nums:
            nums.pop()
        for i in s:
            nums.append(i)
        nums.sort()
        return len(nums)
            