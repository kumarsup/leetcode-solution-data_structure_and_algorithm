class Solution:
    def isValid(self, s: str) -> bool:
        start = "({["
        end = {")": "(", "}": "{", "]": "["}

        stack = []
        for x in s:
            if x in start:
                stack.append(x)
            elif x in end:
                if len(stack) > 0 and end[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0