#482. License Key Formatting
#Question link : https://leetcode.com/problems/license-key-formatting/
#You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

#Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

#Given a non-empty string S and a number K, format the string according to the rules described above.

#Example 1:
#Input: S = "5F3Z-2e-9-w", K = 4
#Output: "5F3Z-2E9W"

#Explanation: The string S has been split into two parts, each part has 4 characters. Note that the two extra dashes are not needed and can be removed.

#Example 2:
#Input: S = "2-5g-3-J", K = 2
#Output: "2-5G-3J"


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper()
        S = ("").join(S.split("-"))

        if len(S)< K:
            return S

        prep =""
        if (len(S) % K != 0):
            prep = S[0:len(S) % K]
            S = S[len(S) % K:len(S)]

        main =("-").join([S[i:i+K] for i in range ( 0, len(S), K)])

        return (prep+"-"+main if prep else main)

#Runtime: 40 ms, faster than 98.79% of Python3 online submissions for License Key Formatting.
#Memory Usage: 13.8 MB, less than 38.02% of Python3 online submissions for License Key Formatting
