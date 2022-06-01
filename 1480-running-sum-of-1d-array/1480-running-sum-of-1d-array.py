class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        a=[]
        for i in nums:
            s+=i
            a.append(s)
        return a