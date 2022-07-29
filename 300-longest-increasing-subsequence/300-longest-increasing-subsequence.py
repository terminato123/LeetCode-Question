class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[0 for i in range(len(nums))]
        n=len(nums)
        maxr1=0
        for i in range(n):
            maxr=0
            for j in range(i):
                if nums[i]>nums[j] and lis[j]>maxr:
                    maxr=lis[j]
            lis[i]=maxr+1
            if lis[i]>maxr1:
                maxr1=lis[i]
        return maxr1
        