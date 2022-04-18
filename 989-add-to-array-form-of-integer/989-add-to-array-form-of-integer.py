class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=''
        a=[]
        for i in num:
            s+=str(i)
        m=int(s)+k
        m=str(m)
        for j in m:
            a.append(int(j))
        return a
        