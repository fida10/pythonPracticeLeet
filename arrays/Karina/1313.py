# 1313. Decompress Run-Length Encoded List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            temp = [nums[i + 1]] * (nums[i])
            ans = ans + temp

        return ans
