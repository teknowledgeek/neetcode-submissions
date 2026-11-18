class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows, cols = len(matrix), len(matrix[0])
        rowHead = False
        colHead = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0 :

                    if r > 0 :
                        if c == 0 :
                            colHead = True
                        # print(matrix)
                        matrix[0][c] = 0
                        # print(matrix)
                        matrix[r][0] = 0
                    else:
                        if c == 0 :
                            colHead = True
                        rowHead = True
        # print(matrix)

        for r in range(rows):
            if matrix[r][0] == 0:
                if r > 0:
                    for c in range(cols):
                        matrix[r][c] = 0
                
        for c in range(cols):

            if matrix[0][c] == 0:
                if c > 0 :
                    for r in range(rows):
                        matrix[r][c] = 0
        print(rowHead)
        print(colHead)
        if rowHead:
            for c in range(cols):
                matrix[0][c] = 0
        if colHead :
            for r in range(rows):
                matrix[r][0] = 0
                


        
        