class Solution:

    def binarysearch(self, lst, target):

        low, high = 0, len(lst) - 1

        while low <= high:
            mid = (low + high)//2

            if target == lst[mid]:
                return True

            elif target < lst[mid]:
                high -= 1
            else:
                low += 1

        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # low, high = (0,0), (len(matrix), len(matrix[0]))

        # lst = []
        # for row in matrix:
        #     lst.extend(row)
        
        # return self.binarysearch(lst, target)
        

        ROWS, COLS = len(matrix), len(matrix[0])
        # find which row its in 

        top = 0
        bottom = ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # find column
        row = (top + bottom)//2

        l, r = 0, COLS - 1

        if not top <= bottom:
            return False
        while l <= r:
            mid = (l + r)//2

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1

            else:
                return True

        return False


        
