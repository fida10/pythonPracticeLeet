class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newNums = [None] * len(nums);
        for i in range(0, len(nums)):
            newNums[i] = nums[nums[i]];

        return newNums;