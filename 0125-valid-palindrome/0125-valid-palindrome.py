class Solution(object):
    def isPalindrome(self, s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())

        if cleaned==cleaned[::-1]:
            return True
        else:
            return False    
        