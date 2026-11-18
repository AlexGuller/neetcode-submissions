class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return actual numbers NOT IDXs
        res = []
        firstIdx = 0
        nums.sort()
        while firstIdx < len(nums) - 2:
            firstVal = nums[firstIdx]
            if firstVal > 0:
                break
            lt = firstIdx + 1
            rt = len(nums) - 1
            while lt < rt:
                secondVal = nums[lt]
                thirdVal = nums[rt]
                if firstVal + secondVal + thirdVal == 0:
                    res.append([firstVal, secondVal, thirdVal])
                    #skip dupes
                    while lt < rt and nums[lt + 1] == nums[lt]:
                        lt += 1
                    lt += 1
                    while lt < rt and nums[rt - 1] == nums[rt]:
                        rt -= 1
                    rt -= 1
                elif firstVal + secondVal + thirdVal < 0:
                    lt += 1
                else:
                    rt -= 1
            while firstIdx < len(nums) - 2 and nums[firstIdx + 1] == nums[firstIdx]:
                firstIdx += 1
            firstIdx += 1
        return res