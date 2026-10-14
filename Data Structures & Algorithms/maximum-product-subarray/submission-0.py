class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        currProd = 1
        for i in range(len(nums)):
            currProd = currProd * nums[i]
            maxProd = max(maxProd, currProd)

            if nums[i] == 0:
                currProd = 1

        currProd = 1
        for i in range(len(nums) - 1, -1, -1):
            currProd = currProd * nums[i]
            maxProd = max(maxProd, currProd)

            if nums[i] == 0:
                currProd = 1
        return maxProd