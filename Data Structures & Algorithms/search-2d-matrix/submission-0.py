class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        top = 0
        bottom = len(matrix) -1


        while top < bottom:

            mid = (top + bottom)// 2

            if matrix[mid][-1] < target :

                top = mid + 1

            else:
                bottom = mid

        if matrix[bottom][-1] >= target:

            l = 0
            r = len(matrix[bottom]) - 1

            while l < r:

                middle = (l + r) // 2

                if matrix[bottom][middle] < target :

                    l = middle + 1
                else:
                    r =middle

            
            if matrix[bottom][r] == target :

                return True


            else : 
                return False

        else:
            return False