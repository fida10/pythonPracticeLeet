# 905. Sort Array By Parity
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        temp = 0
        even = []
        odd = []

        for num in nums:

            if len(nums) == 1 and nums == 0:
                return (0)

            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return (even + odd)
