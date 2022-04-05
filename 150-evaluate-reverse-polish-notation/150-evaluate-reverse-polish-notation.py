class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for element in tokens:

            if element == '+':
                second = stack.pop()
                stack.append(stack.pop() + second)
            elif element == '-':
                second = stack.pop()
                stack.append(stack.pop() - second)
            elif element == '*':
                second = stack.pop()
                stack.append(stack.pop() * second)
            elif element == '/':
                second = stack.pop()
                stack.append(int(stack.pop() / second))

            else:
                stack.append(int(element))

        return stack[-1]
                
            
        