# 1748. Sum of Unique Elements
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        LN = len(nums)
        temp = 0
        for i in range(0, LN):
            temp = nums[i]
            for j in range((i + 1), LN):
                if temp == nums[j]:
                    nums[i] = 0
                    nums[j] = 0

        return (sum(nums))