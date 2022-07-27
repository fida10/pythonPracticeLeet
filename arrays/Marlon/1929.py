class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_num=[None]*len(nums)*2;
        for i in range(0, len(new_num)):
            if i < len(nums):
                new_num[i]=nums[i];
            else :
                new_num[i]=nums[i-len(nums)];
        return new_num