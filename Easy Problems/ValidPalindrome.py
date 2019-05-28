#125. Valid Palindrome
#Problem Link = https://leetcode.com/problems/valid-palindrome/
#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false


class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = re.sub('[^a-z0-9]','', s)
        r = s[::-1]
        if (r==s):
            return True
        else:
            return False


#Runtime: 40 ms, faster than 99.54% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 14.9 MB, less than 17.00% of Python3 online submissions for Valid Palindrome
