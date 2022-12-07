# 2177. Find Three Consecutive Integers That Sum to a Given Number
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        counter = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and ((i * j) % k) == 0:
                    counter += 1

        return counter