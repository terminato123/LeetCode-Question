class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k=len(nums)
        s=set(nums)
        a=[]
        for i in range(1,k+1):
            if i  not in s:
                a.append(i)
        return a
            
        