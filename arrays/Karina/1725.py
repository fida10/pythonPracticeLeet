#1725. Number Of Rectangles That Can Form The Largest Square

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lengths = [0]*len(rectangles)
        counter =0
        for i in range(0, len(rectangles)):
            lengths[i] = min(rectangles[i])
        maxrec = max(lengths)
        for length in lengths:
            if length == maxrec:
                counter += 1
        return counter