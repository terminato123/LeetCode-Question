class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        r=[]
        for i in nums:
            if i%2==0:
                res.append(i)
            else:
                r.append(i)
        return res+r
        