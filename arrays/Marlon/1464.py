class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=max(nums)
        nums.remove(max1)
        max2=max(nums)
        output=(max1-1)*(max2-1)
        return output