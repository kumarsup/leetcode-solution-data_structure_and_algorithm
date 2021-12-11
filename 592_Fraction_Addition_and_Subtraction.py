'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.



Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
Example 4:

Input: expression = "5/3+1/3"
Output: "2/1"


Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''


class Solution:
    def fractionAddition(self, exp: str) -> str:
        if not exp: return "0/1"
        if exp[0] != "-":
            exp = "+" + exp

        i, pos, num, den, = 0, True, [], []

        while i < len(exp):
            pos = True if exp[i] == '+' else False
            i += 1
            n = 0
            while i < len(exp) and exp[i].isdigit():
                n = n * 10 + int(exp[i])
                i += 1
            num.append(n if pos else -n)

            i += 1
            d = 0
            while i < len(exp) and exp[i].isdigit():
                d = d * 10 + int(exp[i])
                i += 1
            den.append(d)

        denominator = functools.reduce(lambda x, y: x * y, den)

        print(num, den)
        for i, (n, d) in enumerate(zip(num, den)):
            num[i] = n * denominator // d

        numerator = sum(num)
        g = math.gcd(numerator, denominator)
        numerator = numerator // g
        denominator = denominator // g

        return str(numerator) + "/" + str(denominator)

#         if not exp:
#             return "0/1"

#         if exp[0] != '-':
#             exp = "+" + exp

#         pos = True
#         i = 0
#         num = []
#         den = []

#         while i < len(exp):
#             pos = True if exp[i] == '+' else False
#             i+=1
#             n = 0

#             while exp[i].isdigit():
#                 n = n*10 + int(exp[i])
#                 i += 1
#             num.append(n if pos else -n)

#             i+=1
#             d = 0
#             while i < len(exp) and exp[i].isdigit():
#                 d = d*10 + int(exp[i])
#                 i+=1
#             den.append(d)

#         denominator = functools.reduce(lambda x, y: x*y, den)

#         for i,(n,d) in enumerate(zip(num, den)):
#             num[i] = n * denominator // d

#         numerator = sum(num)
#         g = math.gcd(numerator, denominator)
#         numerator = numerator // g
#         denominator = denominator // g

#         return str(numerator) + "/" + str(denominator)


#         if not exp:
#             return "0/1"

#         num = []
#         den = []
#         i = 0
#         pos = True

#         if exp[0] != '-':
#             exp = "+"+exp

#         while i < len(exp):
#             pos = True if exp[i] == '+' else False
#             i+=1
#             n = 0
#             while exp[i].isdigit():
#                 n = n*10 + int(exp[i])
#                 i+=1
#             num.append(n if pos else -n)
#             i += 1
#             d = 0
#             while i < len(exp) and exp[i].isdigit():
#                 d = d*10 + int(exp[i])
#                 i+=1
#             den.append(d)

#         denominator = functools.reduce(lambda x, y: x*y, den)
#         for i,(n,d) in enumerate(zip(num, den)):
#             num[i] = n * denominator // d

#         numerator = sum(num)
#         g = math.gcd(numerator, denominator)
#         numerator = numerator // g
#         denominator = denominator // g
#         return str(numerator) + "/" + str(denominator)
