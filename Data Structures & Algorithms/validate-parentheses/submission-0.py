class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in closers:
                if stack and stack[-1] == closers[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False