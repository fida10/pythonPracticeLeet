class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            value=nums[i+1]
            for j in range(0,freq):
                output.append(value)
        return output