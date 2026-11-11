class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_helper(nums):

            rob1, rob2 = 0,0

            for n in nums:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            print(rob2)
            return rob2

        return max(nums[0], rob_helper(nums[1:]), rob_helper(nums[:-1]))


        