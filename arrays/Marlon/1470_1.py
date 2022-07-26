class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out=[None]*len(nums)
        for i in range(0,n):
            out[i*2]=nums[i]
            out[(2*i)+1]=nums[i+n]
        return out