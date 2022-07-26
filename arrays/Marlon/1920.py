class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[None]*len(nums)
        for i in range(0, len(nums)):
            ans[i] = nums[nums[i]]
        return ans