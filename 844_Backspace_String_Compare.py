'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2, M, N, left, right = [], [], len(s), len(t), 0, 0

        for i in range(M):
            if s[i] != "#":
                stack1.append(s[i])
            elif len(stack1) > 0:
                stack1.pop()

        for i in range(N):
            if t[i] != "#":
                stack2.append(t[i])
            elif len(stack2) > 0:
                stack2.pop()

        return stack1 == stack2