class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt = 0
        rt = len(numbers) - 1
        while lt <= rt:
            if numbers[lt] + numbers[rt] == target:
                return [lt + 1, rt + 1]
            if numbers[lt] + numbers[rt] > target:
                rt -=1
            if numbers[lt] + numbers[rt] < target:
                lt += 1
        return [-1, -1]