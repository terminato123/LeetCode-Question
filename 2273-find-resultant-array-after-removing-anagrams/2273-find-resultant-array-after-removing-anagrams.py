class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        k=[]
        k=[words[0]]
        for i in range(1,len(words)):
            if (sorted(list(words[i])))!=(sorted(list(words[i-1]))):
                k.append(words[i])
        return k
        