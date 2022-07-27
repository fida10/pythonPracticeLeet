def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    time = 0;
    for i in range(1, len(points)):
        xDistance = abs(points[i][0] - points[i - 1][0]);
        yDistance = abs(points[i][1] - points[i - 1][1]);

        time += max(xDistance, yDistance);

    return time;
