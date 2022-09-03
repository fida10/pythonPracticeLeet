#561. Array Partition
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a = nums
        a.sort()
        sums = 0

        for i in range(0, len(a), 2):
            temp = min(a[i], a[i+1])
            sums = sums+temp
        return(sums)
