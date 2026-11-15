class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)+1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 1 if int(s[0]) >= 1 else 0

        for i in range(2,n):# since last digit excluded:
            oneDigit = int(s[i - 1:i])# if i >= 1 else 0

            twoDigit = int(s[i-2 : i]) #if i >= 2 else 0

            # print(oneDigit, twoDigit, i)

            if oneDigit >= 1:
                dp[i] += dp[i-1] 

                # print(dp[i])

            if twoDigit in range(10 , 27): # since last digit excluded:
                dp[i] += dp[i-2]
                # print(dp[i])

        return dp[n-1]