class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        currIdx = 0
        while currIdx < len(nums) - 2:
            lt = currIdx + 1
            rt = len(nums) - 1
            origVal = nums[currIdx]
            if nums[currIdx] > 0:
                break
            while lt < rt:
                if nums[lt] + nums[rt] + origVal == 0:
                    res.append([nums[lt], nums[rt], origVal])

                    # skip dupes
                    while lt < rt and nums[lt + 1] == nums[lt]:
                        lt += 1
                    while lt < rt and nums[rt - 1] == nums[rt]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif nums[lt] + nums[rt] + origVal < 0:
                    lt += 1
                else:
                    rt -= 1
            while currIdx < len(nums) - 2 and nums[currIdx + 1] == nums[currIdx]:
                currIdx += 1
            currIdx += 1
        return res