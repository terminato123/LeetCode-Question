class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr=list(set(nums))
        if 0 in arr:
            arr.remove(0)
        return len(arr)
        