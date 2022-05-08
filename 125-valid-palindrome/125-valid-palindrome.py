class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=""
        for i in range(len(s)):
            if s[i].isalpha()==True or s[i].isdigit()==True:
                k+=s[i]
        if k.lower()==k.lower()[::-1]:
            return True
        else:
            return False
        