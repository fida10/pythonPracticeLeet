class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        largest=0
        output=0
        for i in range(0,len(rectangles)):
            value=min(rectangles[i])
            if value>largest:
                largest=value
        for rectangle in rectangles:
            if min(rectangle)==largest:
                output+=1
        return output