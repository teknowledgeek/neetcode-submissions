class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        # print(intervals)

        res = []
        newInterval = intervals[0]
        for interval in intervals:
            if  interval[0] <= newInterval[-1]:
                newInterval[-1] = max(newInterval[-1],interval[-1])
            else:
                res.append(newInterval)
                newInterval = interval
        res.append(newInterval)


        return res
        