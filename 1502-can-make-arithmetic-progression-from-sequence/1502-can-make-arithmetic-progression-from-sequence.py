class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s=arr[1]-arr[0]
        for i in range(len(arr)-1):
            if s!=arr[i+1]-arr[i]:
                return False
        return True
        
        