#1827. Minimum Operations to Make the Array Increasing
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        aLen = len(nums)
        counter = 0;
        for i in range(0, (aLen - 1)):
            if nums[i] >= nums[i + 1]:
                counter += (abs(nums[i] - nums[i + 1])) + 1
                nums[i + 1] = nums[i + 1] + (abs(nums[i] - nums[i + 1])) + 1

        return (counter)

#Troubleshooting
#nums = [1,5,2,4,1]
#aLen = len(nums)
#counter = 0;
#for i in range(0, (aLen - 1)):
#    if nums[i] >= nums[i + 1]:
#        counter += (abs(nums[i] - nums[i + 1])) + 1
#        nums[i + 1] = nums[i + 1] + (abs(nums[i] - nums[i + 1])) + 1
#print(nums)
#print(counter)
