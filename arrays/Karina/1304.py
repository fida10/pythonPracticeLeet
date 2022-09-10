#1304. Find N Unique Integers Sum up to Zero
class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        while (len(nums)) < n - 1:
            val = len(nums)
            nums.append(val + 1)
            nums.append((val + 1) * (-1))

        if n % 2 != 0:
            nums.append(0)
        # (note two lines were skipped  to make a global return)
        # (note two lines were skipped  to make a global return)
        return (nums)