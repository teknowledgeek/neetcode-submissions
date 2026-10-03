class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start  = 0

        end = len(heights) -1
        maxAmount = []

        while start < end:

            # print(start, end)
            waterAmount = (end - start ) * min(heights[start], heights[end])
            maxAmount.append(waterAmount)

            if heights[start] <= heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1

        return max(maxAmount)
        