class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""  
        for char in s:
            if char in "([{":
                stack += char
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack = stack[:-1]
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack = stack[:-1]
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack = stack[:-1]
        
        return stack == ""