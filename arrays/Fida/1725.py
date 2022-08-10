class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largestPossibleSide = 0;

        for rectangle in rectangles:
            if (min(rectangle) > largestPossibleSide):
                largestPossibleSide = min(rectangle);

        squares = 0;
        for rectangle in rectangles:
            if (min(rectangle) == largestPossibleSide):
                squares += 1;

        return squares;

rectangles = [[5,8],[3,9],[5,12],[16,5]];

largeSmallSide = 0;
for indivRectangle in rectangles:
    currentMinVal = min(indivRectangle);
    if (currentMinVal > largeSmallSide):
        largeSmallSide = currentMinVal;

matchRectangle = 0;
for indivRectangle in rectangles:
    if (largeSmallSide == min(indivRectangle)):
        matchRectangle += 1;

print(matchRectangle)