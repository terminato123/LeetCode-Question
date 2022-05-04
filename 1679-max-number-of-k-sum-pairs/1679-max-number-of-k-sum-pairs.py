class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d={}
        res=0
        for i in nums:
            t=k-i
            if  t in d and d[t]>0:
                d[t]-=1
                res+=1
            else:
                if i not in d:
                    d[i]=0
                d[i]+=1
        return res