class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        k=max(arr)
        return arr.index(k)
        