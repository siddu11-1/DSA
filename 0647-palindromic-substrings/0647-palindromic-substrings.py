class Solution(object):
    def countSubstrings(self, s):
        def is_palindromic(sub):
            return sub==sub[::-1]
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if is_palindromic(s[i:j]):
                    count+=1
        return count


        