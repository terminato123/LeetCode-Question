class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        if len(word1)==0 :
            return word2
        elif len(word2)==0:
            return word1
        s=""
        for i in range(l):
            s+=word1[i]+word2[i]
        if len(word1)>l:
            s+=word1[l:]
        elif len(word2)>l:
            s+=word2[l:]
        return s
            
            
        