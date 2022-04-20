class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sort_list = sorted(d.items(), key = lambda item: item[1], reverse = True)
		
        ans = []
		
        for key, value in sort_list:
            if k > 0:
                ans.append(key)
                k -= 1
				
        return ans
         