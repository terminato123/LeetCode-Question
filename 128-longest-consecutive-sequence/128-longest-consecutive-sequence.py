class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        ans = 0
        arr=nums
        n=len(arr)
        for ele in arr:
            s.add(ele)
        for i in range(n):
            if (arr[i]-1) not in s:

                j = arr[i]
                while(j in s):
                    j += 1
                ans = max(ans, j-arr[i])
        return ans