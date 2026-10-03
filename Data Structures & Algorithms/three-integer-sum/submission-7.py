class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if not nums :
            return None

        nums.sort()
        print(nums)
        threeSumList = []
        def get_triplet( index : int) -> list[int]:
            target = - nums[index]

            left = index + 1 
            right = len(nums) - 1 
            while left < right:
                # print(nums[left], target, nums[right])
                if target ==  nums[left] + nums[right]:
                    triplet = [nums[left] ,nums[i] ,  nums[right]]
                    if triplet not in threeSumList : 
                        threeSumList.append(triplet)
                    left += 1
                    right -= 1
                elif target >  nums[left] + nums[right]:
                    left += 1
                elif target <  nums[left] + nums[right]:
                    right -= 1

        for i in range(0, len(nums)-2):
            get_triplet(i)

        return threeSumList