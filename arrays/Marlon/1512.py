class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    output+=1
        return output