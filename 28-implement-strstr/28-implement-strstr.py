class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=len(haystack)
        m=len(needle)
        if l==0 and m==0:
            return 0
        for i in range(l):
            if haystack[i:i+m]==needle:
                return i
        return -1
        