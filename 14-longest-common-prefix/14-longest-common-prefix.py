class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        p=s[0]
        i=0
        while i<len(s)-1 and len(p)!=0:
            i=0
            for j in range(1,len(s)):
                if s[j].startswith(p):
                    i+=1
                    continue
                else:
                    p=p[:-1]
        return p
        