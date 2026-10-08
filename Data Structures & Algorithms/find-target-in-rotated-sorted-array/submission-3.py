class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0

        r = len(nums) - 1


        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r] :

                l = mid + 1

            else:

                r = mid

        print(l, r)
        if nums[r] <= target  and nums[len(nums) - 1] >= target:

            r = len(nums) - 1
        else:
            l = 0
            r = r - 1
        print(l, r)
        while l < r :
            mid = (l+r) // 2

            if nums[mid] < target :
                l = mid + 1
            else:
                r = mid

        if nums[r] == target :
            return r
        else :
            return -1