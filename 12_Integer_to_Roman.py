'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        num_ = list(str(num))
        print(num_)
        while len(num_) < 4:
            num_ = ['0'] + num_
            print(num_)
        dic_thousand = {'3': 'MMM', '2': 'MM', '1': 'M', '0': ''}
        dic_hundred = {'9': 'CM', '8': 'DCCC', '7': 'DCC', '6': 'DC', '5': 'D', '4': 'CD', '3': 'CCC', '2': 'CC',
                       '1': 'C', '0': ''}
        dic_ten = {'9': 'XC', '8': 'LXXX', '7': 'LXX', '6': 'LX', '5': 'L', '4': 'XL', '3': 'XXX', '2': 'XX', '1': 'X',
                   '0': ''}
        dic_one = {'9': 'IX', '8': 'VIII', '7': 'VII', '6': 'VI', '5': 'V', '4': 'IV', '3': 'III', '2': 'II', '1': 'I',
                   '0': ''}
        result = dic_thousand[num_[0]] + dic_hundred[num_[1]] + dic_ten[num_[2]] + dic_one[num_[3]]
        return result

#         valuesM = {
#             1:'I',
#             2:'II',
#             3:'III',
#             4:'IV',
#             5:'V',
#             6:'VI',
#             7:'VII',
#             8:'VIII',
#             9:'IX',
#             10:'X',
#             40:'XL',
#             50:'L',
#             90:'XC',
#             100:'C',
#             400:'CD',
#             500:'D',
#             900:'CM',
#             1000:'M'
#         }

#         def numLen(num):
#             return len(str(abs(num)))

#         res = ""
#         xxx = [4, 5, 9]

#         def getMaxVal(y, xx):
#             for i in range(len(xx)-1, -1,-1):
#                 if y > xx[i]: return xx[i]
#             return 1

#         while num > 0:
#             digits = numLen(num)
#             if digits == 1:
#                 res += valuesM[num]
#                 num = 0
#             else:
#                 x = 10**(digits-1)
#                 y = num//x
#                 z = x*y
#                 if z in valuesM:
#                     x = z
#                 elif y in xxx:
#                     x = x*y
#                 else:
#                     val = getMaxVal(y, xxx)
#                     x *= val
#                 print(x, y, z, num, res)
#                 num -= x
#                 res = res+valuesM[x]
#         return res