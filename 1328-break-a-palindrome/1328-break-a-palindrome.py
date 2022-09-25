class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2:
            return ""

        for i in range(n//2):
            if palindrome[i] != 'a' and i != n-1-i:
                return palindrome[:i] + 'a' + palindrome[i+1:]

        return palindrome[:-1] + 'b'
        