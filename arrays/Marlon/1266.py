class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(0,len(points)-1):
            deltax=abs(points[i+1][0]- points[i][0])
            deltay=abs(points[i+1][1]- points[i][1])
            time+=max(deltax,deltay)
        return time