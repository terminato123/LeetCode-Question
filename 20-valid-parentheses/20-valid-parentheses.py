class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        a=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if (i=='(' or i=='[' or i=='{'):
                stack.append(i)
            elif(len(stack) == 0):
                return False
            else:
                p = stack.pop()
                if(d[i] != p):
                    return False
        if len(stack)==0:
            return True
        return False
            
        
            
        