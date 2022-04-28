class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l=list(magazine)
        c=0
        for i in ransomNote:
            if i in l:
                l.remove(i)
                c+=1
        if c==len(ransomNote):
            return True
        else:
            return False
            
        
        
        