class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        l=sorted(nums)
        if  len(nums)==1:
            return 0
        elif l[-2]*2<=m:
            return nums.index(m)
        return -1
        
        
        