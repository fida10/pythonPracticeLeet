class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        pairs = 0;
        i = 0;
        end = len(nums);

        while (i < end):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]):
                    nums.pop(j);
                    nums.pop(i);
                    i = -1;
                    pairs += 1;
                    break;
            i += 1;
            end = len(nums);

        return [pairs, len(nums)];