class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output=[]
        for i in range(0,len(index)):
            output.insert(index[i], nums[i])
        return output