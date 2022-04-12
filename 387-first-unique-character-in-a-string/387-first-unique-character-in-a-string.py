class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=[]
        for j in s:
            a.append(j)
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==1:
                k=a.index(i)
                return k
        else:
            return -1
        