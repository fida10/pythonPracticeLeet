class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort();
        smallNo = nums[0];
        largeNo = nums[len(nums) - 1];

        gcd = 0;
        for i in range(1, smallNo + 1):
            if (smallNo % i == 0 and largeNo % i == 0):
                gcd = i;

        return gcd;