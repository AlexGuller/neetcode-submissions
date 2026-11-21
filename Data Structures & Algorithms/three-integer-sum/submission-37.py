class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = 0
        while curr < len(nums) - 2:
            firstVal = nums[curr]
            if firstVal > 0:
                break
            lt = curr + 1
            rt = len(nums) - 1
            while lt < rt:
                #skip dupes
                secondVal = nums[lt]
                thirdVal = nums[rt]
                if firstVal + secondVal + thirdVal == 0:
                    res.append([firstVal, secondVal, thirdVal])
                    while lt < rt and nums[lt] == nums[lt + 1]:
                        lt += 1
                    while lt < rt and nums[rt] == nums[rt - 1]:
                        rt -= 1
                    rt -= 1
                    lt += 1
                elif firstVal + secondVal + thirdVal > 0:
                    rt -= 1
                else:
                    lt += 1
            while curr < len(nums) - 2 and nums[curr] == nums[curr + 1]:
                curr += 1
            curr += 1
        return res
