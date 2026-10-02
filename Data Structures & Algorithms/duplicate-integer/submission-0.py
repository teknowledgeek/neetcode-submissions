class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums is None:
            return False

        i = 0 
        duplicate = [] 

        while i < len(nums):
            if nums[i] not in duplicate:

                duplicate.append(nums[i])
            else :
                return True
            i += 1
        return False