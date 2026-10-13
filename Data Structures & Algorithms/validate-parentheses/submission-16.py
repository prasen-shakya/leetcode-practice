class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        parentheses_map = {'[':']', '{':'}','(':')'}

        for c in s:
            if c in parentheses_map:
                stack.append(parentheses_map[c])
                continue

            if stack and stack[-1] == c:
                stack.pop()
                continue

            return False
                    


        return len(stack) == 0