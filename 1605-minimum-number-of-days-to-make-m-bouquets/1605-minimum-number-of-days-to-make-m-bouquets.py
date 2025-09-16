class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        def isPossible(day):
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        low = min(bloomDay)
        high = max(bloomDay)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
        