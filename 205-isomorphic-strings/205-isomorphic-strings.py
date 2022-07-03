class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(t)!=len(s):
            return False
        for i in range(len(s)):
            if s[i] not in  d:
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
        