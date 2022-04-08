class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k=len(nums)
        d={}
        a=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>(k//3):
                a.append(i)
        return a
                
        