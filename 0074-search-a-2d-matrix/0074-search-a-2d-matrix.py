class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for value in row:
                if value == target:
                    return True
        return False
        