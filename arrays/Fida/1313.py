class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        output = [];
        for i in range(0, len(nums), 2):

            for j in range(0, nums[i]):
                output.append(nums[i + 1]);

        return output;