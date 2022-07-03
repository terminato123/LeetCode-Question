class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        word=s.split()
        if len(pattern)!=len(word):
            return False
        for i in range(len(word)):
            if pattern[i] not in  d:
                if word[i] in d.values():
                    return False
                d[pattern[i]]=word[i]
            else:
                if d[pattern[i]] != word[i]:
                    return False
        return True
                       
        