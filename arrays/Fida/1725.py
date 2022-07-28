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