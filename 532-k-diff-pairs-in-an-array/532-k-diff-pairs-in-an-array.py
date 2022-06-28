class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        a=[]
        d={}
        c=0
        if k>0:
            for i in range(len(nums)):
                if nums[i]+k in nums and k!=0:
                    a.append([nums[i]])
            l=[]
            for i in a:
                if i not in l:
                    l.append(i)
            return len(l)
        else:
            for i in nums:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            for i in d:
                if d[i]>1:
                    c+=1
            return c
                    
                