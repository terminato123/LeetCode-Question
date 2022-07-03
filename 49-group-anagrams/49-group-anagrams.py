class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=[]
        d={}
        c=[]
        for i in strs:
            m="".join(sorted(i))
            if m not in d:
                d[m]=[i]
            else:
                d[m].append(i)
        for i in d.values():
            k.append(i)
        return k
        
        