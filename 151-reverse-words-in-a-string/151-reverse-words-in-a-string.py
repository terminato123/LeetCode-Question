class Solution:
    def reverseWords(self, s: str) -> str:
        a=[]
        for i in s.split():
            a.append(i)
        a=a[::-1]
        return " ".join(a)
        