#1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = [False] * len(candies)
        for i in range(0, len(candies)):
            tempNumCandies = candies[i] + extraCandies
            if tempNumCandies >= max(candies):
                results[i] = True
            else:
                results[i] = False
        return results
