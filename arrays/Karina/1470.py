# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        case = [None] * len(nums)
        temp = 0
        for i in range(0, n):
            case[i * 2] = nums[i]
            case[(i * 2) + 1] = nums[i + n]
            # temp = nums[i+2]
        return case
