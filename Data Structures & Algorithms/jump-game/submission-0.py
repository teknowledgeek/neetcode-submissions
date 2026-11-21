class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finalDestn = len(nums) - 1

        for i in range(len(nums)-1, -1,-1):
            maxJump = nums[i]
            jump = 0
            while jump <= maxJump:
                # print(i,jump, maxJump, finalDestn)
                if i+jump == finalDestn:
                    finalDestn = i
                    break
                else:
                    jump += 1

        if finalDestn == 0:
            return True
        else:
            return False
        