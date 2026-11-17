class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key= lambda x: x[-1])

        count = 0

        # print(intervals)

        prevEnd = float("-inf")

        for interval in intervals:

            print(prevEnd)

            if interval[0] < prevEnd:
                count += 1

            else:
                prevEnd = interval[-1]



        return count
        