#961. N-Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        temp =0
        for num in nums:
            temp = nums.count(num)
            if temp > 1:
                return(num)
