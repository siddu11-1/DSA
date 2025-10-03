class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        result = []

        while top <= bottom and left <= right:
            # Traverse top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse bottom row (if still within bounds)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse left column (if still within bounds)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result