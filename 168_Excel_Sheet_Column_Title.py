'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
Example 4:

Input: columnNumber = 2147483647
Output: "FXSHRXW"


Constraints:

1 <= columnNumber <= 231 - 1
'''


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            print(columnNumber, remainder)
            title = alphabet[remainder] + title
        return title

#         d = {
#             1:'A',
#             2:'B',
#             3:'C',
#             4:'D',
#             5:'E',
#             6:'F',
#             7:'G',
#             8:'H',
#             9:'I',
#             10:'J',
#             11:'K',
#             12:'L',
#             13:'M',
#             14:'N',
#             15:'O',
#             16:'P',
#             17:'Q',
#             18:'R',
#             19:'S',
#             20:'T',
#             21:'U',
#             22:'V',
#             23:'W',
#             24:'X',
#             25:'Y',
#             0:'Z'
#         }

#         ret = ''
#         while columnNumber > 0:
#             ret = d[columnNumber % 26]+ret
#             if columnNumber % 26 == 0:
#                 columnNumber -= 26
#             columnNumber = columnNumber // 26
#         print(ret)
#         return ret


# res = ""
# while n > 0:
#     char = chr(ord('A')+((n-1)%26))
#     res = char+res
#     n = (n-1)//26
# return res