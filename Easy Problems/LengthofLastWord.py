#58. Length of Last Word
# Problem Link: https://leetcode.com/problems/length-of-last-word/
#Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#If the last word does not exist, return 0.

#Note: A word is defined as a character sequence consists of non-space characters only.

#Example:

#Input: "Hello World"
#Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.strip() == '':
            return 0
        lastword=s.strip().split(' ')[-1]
        return len(lastword) if lastword!= '' else 1

#Runtime: 36 ms, faster than 86.84% of Python3 online submissions for Length of Last Word.
#Memory Usage: 13.1 MB, less than 68.81% of Python3 online submissions for Length of Last Word
