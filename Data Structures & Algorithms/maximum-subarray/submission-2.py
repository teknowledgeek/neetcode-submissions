class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        maxSoFar = float("-inf")
        curMax = 0
        # sumArray = [maxSoFar]*len(nums)
        # print(sumArray)

        for i in range(len(nums)):

            # maxSoFar = maxSoFar if maxSoFar > float("-inf") else 0
            curMax = max(nums[i], nums[i]+ curMax)

            # while cur <= i:
            #     sumArray[cur] = sumArray[cur] + nums[i] if sumArray[cur] > float("-inf") else nums[i]
            #     cur += 1
            maxSoFar = max(maxSoFar, curMax)

            # print(maxSoFar, curMax)


        # print(sumArray)

        return maxSoFar


        