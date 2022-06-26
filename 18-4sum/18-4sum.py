class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                n=len(nums)-1
                while(k<n):
                    c=nums[i]+nums[j]+nums[k]+nums[n]
                    if c==target:
                        a.append([nums[i],nums[j],nums[k],nums[n]])
                        k+=1
                        n-=1
                    elif c<target:
                        k+=1
                    else:
                        n-=1
        m=[]
        for i in a:
            if i not in m:
                m.append(i)
        return m
        