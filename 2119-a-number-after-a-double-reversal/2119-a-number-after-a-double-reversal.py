class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        k=str(num)
        k=k[::-1]
        k=int(k)
        k=str(k)[::-1]
        if int(k)==num:
            return True
        else:
            return False
        
        