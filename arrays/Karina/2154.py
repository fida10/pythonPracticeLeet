# 2154. Keep Multiplying Found Values by Two
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        counter = 0

        while original in nums:
            original = original * 2

        return (original)
