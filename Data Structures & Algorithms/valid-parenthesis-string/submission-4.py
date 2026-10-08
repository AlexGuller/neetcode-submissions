class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for ch in s:
            if ch == '(':
                leftMin += 1
                leftMax += 1
            elif ch == ')':
                leftMin -= 1
                leftMax -=1
            else:
                leftMin -= 1 # '*' -> ')'
                leftMax += 1 # '*' -> '('
            # if at any point more ')' than '(' not possible
            if leftMax < 0:
                return False
            leftMin = max(0, leftMin)
        return leftMin == 0