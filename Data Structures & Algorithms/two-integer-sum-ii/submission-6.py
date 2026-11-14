class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #inc order
        lt, rt = 0, len(numbers) - 1
        while lt < rt:
            if numbers[lt] + numbers[rt] == target:
                return [lt + 1, rt + 1]
            elif numbers[lt] + numbers[rt] < target:
                lt += 1
            else:
                rt -= 1
        return [-1, -1]