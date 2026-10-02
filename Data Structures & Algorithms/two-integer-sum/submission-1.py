class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0

        while i < len(nums):
            if (target - nums[i]) in nums :
                j = nums.index(target - nums[i])

                if j > i:
                    return [i, j]
                elif j  < i :
                    return [j,i]

            i += 1


        return None