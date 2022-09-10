# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j and nums[i] > nums[j]:
                    count[i] += 1
        return count


