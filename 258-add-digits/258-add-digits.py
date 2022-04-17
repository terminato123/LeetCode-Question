class Solution:
    def addDigits(self, num: int) -> int:
        k=str(num)
        if len(str(num))==1:
            return num
        while len(k)>1:
            s=0
            for i in k:
                s+=int(i)
            k=str(s)
        return int(k)
        