class Solution(object):
    def canChange(self, start, target):
        if start.replace('_', '') != target.replace('_', ''):
            return False

        n = len(start)
        i = j = 0

        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            if i == n and j == n:
                return True
            if i == n or j == n:
                return False

            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True