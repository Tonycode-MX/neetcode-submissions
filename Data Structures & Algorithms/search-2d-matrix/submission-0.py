class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0])
        ROWS = len(matrix)

        def rowSearcher(up, down):
            if up > down:
                return -1
            
            mid = (up+down) //2

            lastUp = matrix[mid][-1]
            firstDown = matrix[mid][0]

            if firstDown <= target <= lastUp:
                return mid
            
            elif target < firstDown:
                return rowSearcher(up, mid-1)

            elif target > lastUp:
                return rowSearcher(mid+1, down)

        def numSearcher(row_idx, left,right):
            if left > right:
                return False
            
            mid = (right + left) // 2

            if matrix[row_idx][mid] == target:
                return True

            elif matrix[row_idx][mid] < target:
                return numSearcher(row_idx, mid+1, right)
            
            elif matrix[row_idx][mid] > target:
                return numSearcher(row_idx, left, mid-1)

        target_row = rowSearcher(0, ROWS - 1)

        if target_row == -1:
            return False

        return numSearcher(target_row, 0, COLS-1)


        
        