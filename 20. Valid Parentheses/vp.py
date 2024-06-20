class Solution(object):        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        mapi = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            if char in opening:
                stack.append(char)
            
            elif char in closing and mapi.get(char, None) == stack[0]:
                stack.pop(0)
            
            else:
                return False         
        return True
    
s = Solution()

assert s.isValid(s = "{}[]()") == True
assert s.isValid(s = "()") == True
assert s.isValid(s = "(]") == False
assert s.isValid(s = "{[]()}") == True
assert s.isValid("([)]") == False