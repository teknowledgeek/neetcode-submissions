class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        moveMatrix = [[1]*n]*m
        # print(moveMatrix)
        for i in range(m):
            for j in range(n):
                if i ==0 :
                    moveMatrix[i][j] = 1
                elif j == 0:
                    moveMatrix[i][j] = 1

                else :
                    moveMatrix[i][j] = moveMatrix[i-1][j] + moveMatrix[i][j-1]
                # print(moveMatrix)

        return moveMatrix[m-1][n-1]

        