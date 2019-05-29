#9. Palindrome Number
#Problem Link = https://leetcode.com/problems/palindrome-number/
#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#Follow up:
            #Coud you solve it without converting the integer to a string?
#Example 1:
#Input: 121
#Output: true

#Example 2:
#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#Example 3:
#Input: 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y=[]

        while x!=0:
            temp=x%10
            x //=10
            y += [temp]

        return y == y[::-1]

#Runtime: 76 ms, faster than 89.59% of Python3 online submissions for Palindrome Number.
#Memory Usage: 13.2 MB, less than 70.82% of Python3 online submissions for Palindrome Number.
