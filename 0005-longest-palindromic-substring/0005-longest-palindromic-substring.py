"""class Solution(object):
    def longestPalindrome(self, s):
        longest=" "
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                substring=s[i:j]
                if substring==substring[::-1] and len(substring)>len(longest):
                    substring=longest
        return longest """
class Solution(object):
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > len(longest):
                    longest = substring
        return longest                               

        