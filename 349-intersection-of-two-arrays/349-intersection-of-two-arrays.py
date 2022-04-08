class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        a=[]
        for i in nums1:
            if i in nums2:
                a.append(i)
        return a
                
        