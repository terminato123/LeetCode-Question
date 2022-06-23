class Solution:
    def greatestLetter(self, s: str) -> str:
        c="abcdefghijklmnopqrstuvwxyz"
        l=[""]
        for i in c:
            if i in s and i.upper() in s:
                l.append(i.upper())
        l.sort()
        return l[-1]
        