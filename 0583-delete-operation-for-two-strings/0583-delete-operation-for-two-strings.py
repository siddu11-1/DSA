class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        lcs_length=dp[m][n]
        return (m-lcs_length)+(n-lcs_length)
        