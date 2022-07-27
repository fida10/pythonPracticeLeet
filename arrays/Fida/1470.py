class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = [None] * len(nums);

        for i in range(0, n):
            newNums[i * 2] = nums[i];
            newNums[(i * 2) + 1] = nums[i + n];

        return newNums;