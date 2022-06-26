class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                c=nums[i]+nums[j]+nums[k]
                if c==0:
                    a.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif c<0:
                    j+=1
                else:
                    k-=1
        m=[]
        for i in a:
            if i not in m:
                m.append(i)
        return m
                    
            
            
        
                
                            
                            
                            
                    
                
        