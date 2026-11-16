class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n  = len(nums)
        leftProduct = 1
        rightProduct = 1
        res = float('-inf')

        for i in range(n):
            leftProduct = 1 if leftProduct == 0 else leftProduct
            rightProduct = 1 if rightProduct == 0 else rightProduct

            leftProduct *= nums[i]
            rightProduct *= nums[n -1 - i]

            res = max(res, leftProduct, rightProduct)
        return res
        