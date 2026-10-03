class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        consecutive_list = [0]
        consecutive = 1
        start_sequence = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == start_sequence + 1 :
                consecutive += 1 
                start_sequence = nums[i]
            elif nums[i] > start_sequence + 1 :
                start_sequence = nums[i]
                consecutive_list.append(consecutive)
                consecutive = 1
        
        consecutive_list.append(consecutive)
        return max(consecutive_list)

        