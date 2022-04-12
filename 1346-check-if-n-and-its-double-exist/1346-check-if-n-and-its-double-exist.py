class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c=0
        for i in arr:
            if i==0:
                c+=1
        if c>=2:
            return True
        for i in arr:
            if 2*i in arr and i!=0:
                return True
        else:
            return False
        