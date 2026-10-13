class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        parentheses_map = {'[':']', '{':'}','(':')'}

        for c in s:
            if c in {'[', '(','{'}:
                stack.append(parentheses_map[c])
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
                    


        return len(stack) == 0