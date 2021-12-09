'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra
spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be
left-justified instead of fully-justified. Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

Solution:
Input -
words - maxLen

Step1:
    - totalTen  = len of the string can be formed + spaces needed in the string + 1
    - minLines =  totalTen//maxLen

Step2:
    - iterate on the words and keep adding the word untill we reach to the maxLen
        - if len(s) + spaces + word < maxlen: add the word to s
        - else: Step3

Step3:
    - Add to result and flus the curr formed string
    - Add the spaces from left to right if not last line

Step4:
    - Return the results
'''


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words: return words
        res, curr, no_of_letters = [], [], 0

        for word in words:
            if no_of_letters + len(curr) + len(word) > maxWidth:
                if len(curr) == 1:
                    res.append(curr[0] + " " * (maxWidth - no_of_letters))
                else:
                    num_spaces = maxWidth - no_of_letters
                    space_between_word, extra = divmod(num_spaces, len(curr) - 1)
                    for i in range(extra): curr[i] += " "
                    res.append((" " * space_between_word).join(curr))
                curr = []
                no_of_letters = 0
            curr.append(word)
            no_of_letters += len(word)
        res.append(" ".join(curr) + " " * (maxWidth - no_of_letters - len(curr) + 1))
        return res

