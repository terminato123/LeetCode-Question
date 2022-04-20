class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        arr=[]
        for i in letters:
            arr.append(ord(i))
        k=ord(target)
        for i in arr:
            if (i<=k):
                continue
            else:
                return (chr(i))
        j=(max(arr))
        if (k>=j):
            return (chr(min(arr)))
        
        