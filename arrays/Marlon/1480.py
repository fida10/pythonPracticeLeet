class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newnums=[None]*len(nums)
        newnums[0]=nums[0]
        for i in range(1,len(nums)):
            newnums[i]=newnums[i-1]+nums[i]
        return newnums