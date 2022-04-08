class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=0
        for i in d:
            if m<d[i]:
                m=d[i]
        for i in d:
            if d[i]==m:
                return i
        