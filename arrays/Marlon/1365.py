class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller=[]
        for i in range(0, len(nums)):
            issmaller=0
            for j in range(0, len(nums)):
                if nums[j] < nums[i]:
                    issmaller+=1
            smaller.append(issmaller)
        return smaller