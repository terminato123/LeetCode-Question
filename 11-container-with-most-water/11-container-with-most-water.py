class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg=0
        end=len(height)-1
        area=0
        while beg<end:
            area=max(area,min(height[beg],height[end])*(end-beg))
            if height[beg]>=height[end]:
                end-=1
            else:
                beg+=1
        return area
        