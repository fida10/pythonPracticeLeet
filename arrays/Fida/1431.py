class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxCandies = [];

        for i in range(len(candies)):
            hasMax = True;
            currentKid = candies[i] + extraCandies;
            for j in range(len(candies)):
                if (candies[j] > currentKid):
                    hasMax = False;
                    break;
            maxCandies.append(hasMax);

        return maxCandies;