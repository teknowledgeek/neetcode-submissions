class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []

        rowBegin, rowEnd = 0, len(matrix) - 1
        colBegin, colEnd = 0, len(matrix[0]) - 1


        while rowBegin <= rowEnd and colBegin <= colEnd:
            # print(rowBegin, rowEnd, colBegin, colEnd)
            # print("turnLeft")
            for i in range(colBegin, colEnd + 1):
                # print(rowBegin, i)
                path.append(matrix[rowBegin][i])

            # print(path)
            rowBegin += 1

            # print("turnDown")
            for i in range(rowBegin, rowEnd + 1):
                # print(i, colEnd)
                path.append(matrix[i][colEnd])

            # print(path)
            colEnd -= 1

            # print("turnRight")
            # print(rowBegin, rowEnd, colBegin, colEnd)
            if colBegin <= colEnd and rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    # print(rowEnd, i)
                    path.append(matrix[rowEnd][i])

                # print(path)
                rowEnd -= 1

            # print("turnUP")
            if colBegin <= colEnd and rowBegin <= rowEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    path.append(matrix[i][colBegin])

                # print(path)
                colBegin += 1
            # print(rowBegin, rowEnd, colBegin, colEnd)

        return path


        