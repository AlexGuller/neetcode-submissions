class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = 0
        nums.sort()
        while curr < len(nums) - 2:
            if nums[curr] > 0:
                break
            lt = curr + 1
            rt = len(nums) - 1
            while lt < rt:
                if nums[curr] + nums[lt] + nums[rt] == 0:
                    res.append([nums[curr],nums[lt],nums[rt]])
                    # skip left dupes
                    while lt < rt and nums[lt] == nums[lt + 1]:
                        lt += 1
                    lt += 1
                    #skip right
                    while lt < rt and nums[rt] == nums[rt - 1]:
                        rt -= 1
                    rt -= 1
                elif nums[curr] + nums[lt] + nums[rt] > 0:
                    rt -= 1
                else:
                    lt += 1
            # skip curr dupes
            while curr < len(nums) - 2 and nums[curr] == nums[curr + 1]:
                curr += 1
            curr += 1
        return res