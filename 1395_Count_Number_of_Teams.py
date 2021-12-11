'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res, n = 0, len(rating)
        if n < 3: return 0

        for i in range(n):
            lowL, highL, lowR, highR = 0, 0, 0, 0
            j = i - 1
            while j >= 0:
                if rating[j] < rating[i]:
                    lowL += 1
                else:
                    highL += 1
                j -= 1

            j = i + 1
            while j < n:
                if rating[j] > rating[i]:
                    highR += 1
                else:
                    lowR += 1
                j += 1
            res += lowL * highR + highL * lowR

        return res

#         up = [0] * n
#         down = [0] * n

#         teams = 0
#         for j in range(n):
#             for i in range(j):
#                 if rating[i] < rating[j]:
#                     up[j] += 1
#                     teams += up[i]
#                 else:
#                     down[j] += 1
#                     teams += down[i]
#         return teams

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
#                 count += 1
# return count


#         for j in range(1, n-1):
#             i, k = j-1, j+1

#             while i >= 0:
#                 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
#                     count += 1
#                 i -= 1

#             while k < n:
#                 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
#                     count += 1
#                 k += 1

#         return count



