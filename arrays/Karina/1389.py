#1389. Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(0, len(nums)):
            # Note: list.insert(i, elem)
            target.insert(index[i], nums[i])
        return target
