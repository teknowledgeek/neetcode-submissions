class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        
        print(text1, text2)
        matrix = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        print(matrix)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2)-1,-1,-1):
            
                # print(i, j)
                # print(matrix)
                if text1[i] == text2[j]:
                    # print(i, j,matrix[i][j])
                    matrix[i][j] = 1+matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i][j+1], matrix[i+1][j])
        print(matrix)
        return matrix[0][0]


        