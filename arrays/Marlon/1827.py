class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                count+=(nums[i-1]-nums[i])+1
                nums[i]+=(nums[i-1]-nums[i])+1
        return count