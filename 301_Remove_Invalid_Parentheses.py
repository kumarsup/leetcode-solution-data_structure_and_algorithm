'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]

Constraints:
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        maxLan, res = -1, set()

        def valid_parantheses(val):
            count = 0
            for ch in val:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                if count < 0: return False
            return count == 0

        def backtrack(val, seen, idx=0):
            nonlocal maxLan, res

            if valid_parantheses(val) and maxLan <= len(val):
                print(val, maxLan, len(val))
                res.add("".join(val))
                maxLan = len(val)
                return

            for i in range(idx, len(val)):
                if i not in seen and val[i] in ['(', ')']:
                    seen.add(i)
                    backtrack(val[:i] + val[i + 1:], seen, i + 1)
                    seen.remove(i)

        backtrack(list(s), set())
        maxLen = -1
        for val in res:
            maxLen = max(maxLen, len(val))
        result = []
        for val in res:
            if maxLen == len(val):
                result.append(val)
        return result if len(result) > 0 else [""]