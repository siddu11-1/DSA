import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        def isp(speed):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / float(speed))
            return total_hours <= h

        low = 1
        high = max(piles)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isp(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result