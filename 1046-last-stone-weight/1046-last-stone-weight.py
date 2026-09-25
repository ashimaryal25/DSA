import heapq

class Solution(object):
    def lastStoneWeight(self, stones):

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            x = -heapq.heappop(heap)   # largest
            y = -heapq.heappop(heap)   # second largest

            if x != y:
                heapq.heappush(heap, -(x - y))

        if heap:
            return -heap[0]

        return 0 
        