class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        subList = [1] * len(nums)


        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    # print(i, j , subList, nums)
                    subList[i] = max(subList[i],subList[j]+1) 

        return max(subList)
        