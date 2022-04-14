class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s=0
        l,r=0,int(sqrt(c))
        while l<=r:
            s=l**2+r**2
            if s==c:
                return True
            elif s<c:
                l+=1
            else:
                r-=1
        return False

        