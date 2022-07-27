class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        morecandy=[]
        maximum=max(candies)
        for i in range(0,len(candies)):
            maxcandy=candies[i]+extraCandies
            if maxcandy>=maximum:
                morecandy.append(True)
            else:
                morecandy.append(False)
        return morecandy