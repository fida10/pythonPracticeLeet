class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        newNums = [None] * len(nums) * 2;

        for i in range(0, len(newNums)):
            if i < len(nums):
                newNums[i] = nums[i];
            else:
                newNums[i] = nums[i - len(nums)];

        return newNums;