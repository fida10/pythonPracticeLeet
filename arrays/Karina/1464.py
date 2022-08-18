#1464. Maximum Product of Two Elements in an Array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1st = max(nums)
        nums.remove(max1st)
        max2nd = (max(nums))
        return (max1st - 1) * (max2nd - 1)

    ## Sacp