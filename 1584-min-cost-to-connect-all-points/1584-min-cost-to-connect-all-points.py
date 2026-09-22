import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        dist = []

        heapq.heappush(dist, (0,0))
        seen = set()

        total = 0
        while len(seen) < n:
            cost, point = heapq.heappop(dist)

            if point in seen:
                continue

            seen.add(point)
            total += cost

            x1, y1 = points[point]
            for i in range(n):

                if i in seen:
                    continue
                x2, y2 = points[i]
                d = abs(x2 - x1) + abs(y2 - y1)

                heapq.heappush(dist,(d,i))
        return total


