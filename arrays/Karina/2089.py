#2089. Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        indexes = []
        nums.sort()

        for i in range(0, len(nums)):
            if target == nums[i]:
                indexes.append(i)
        return (indexes)

    """ nums = [1,2,5,2,3]
        lenArr = len(nums)
        indexes = []*lenArr
        nums.sort()
        counter = 0
        for i in range(0, lenArr):
            if target == nums[i]:
                indexes[counter] = i
                counter += 1
        print(indexes)
       """