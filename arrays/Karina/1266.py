1266. Minimum Time Visiting All Points
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        numsteps = 0
        for i in range(0, (len(points)-1)):
            deltax = abs(points[i+1][0] - points[i][0])
            deltay = abs(points[i+1][1] - points[i][1])
            numsteps +=  max(deltax, deltay)
        return numsteps
