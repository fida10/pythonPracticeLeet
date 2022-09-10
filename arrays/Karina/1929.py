# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        y = len(nums)
        ans = [None] * len(nums) * 2
        # for i loop
        # for i in range(start, end,step)
        # for each would be for num in nums:
        for i in range(0, len(nums)):
            ans[i] = nums[i]
            ans[i + y] = nums[i]
        return (ans)
