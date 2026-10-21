class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to fi correct row
        #binary search in row to fin correct index
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                #niether means were on the correct row
                break

        if top > bottom: #if ptrs have crossed, target is not in the matrix
            return False

        r = (top + bottom ) // 2
        #binary search on the row
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[r][mid] == target:
                return True
            if matrix[r][mid] < target: #update boundaries for next search area
                left = mid + 1
            else:
                right = mid - 1
        return False

        # time: O(logm + logn) = O(log(n * m))
        # space: O(1)



