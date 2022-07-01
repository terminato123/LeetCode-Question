class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ug=[1]
        t=0
        th=0
        f=0
        while len(ug)<n:
            b1=ug[t]*2
            b2=ug[th]*3
            b3=ug[f]*5
            minimum=min(b1,b2,b3)
            ug.append(minimum)
            if minimum==b1:
                t+=1
            if minimum==b2:
                th+=1
            if minimum==b3:
                f+=1
        return ug[-1]
            
            
        