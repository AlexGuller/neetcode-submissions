class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = 0
        while curr < len(nums) - 2:
            if nums[curr] > 0:
                break
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue
            lt = curr + 1
            rt = len(nums) - 1
            while lt < rt:
                if nums[curr] + nums[lt] + nums[rt] == 0:
                    res.append([nums[curr],nums[lt],nums[rt]])
                    # rem dupes
                    while lt < rt and nums[lt + 1] == nums[lt]:
                        lt += 1
                    while lt < rt and nums[rt - 1] == nums[rt]:
                        rt -= 1
                    lt += 1
                    rt -= 1
                elif nums[curr] + nums[lt] + nums[rt] < 0:
                    lt += 1
                else:
                    rt -= 1
            curr += 1
        return res
                