class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}

        for b in s:
            if b in mapping:
                if len(stack) == 0 or stack[-1] != mapping[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)
        
        return len(stack) == 0 