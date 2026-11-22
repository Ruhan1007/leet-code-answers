
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = []
        heap = [(0, float('inf'))]

        for x, neg_height, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)

            if neg_height:
                heapq.heappush(heap, (neg_height, right))

            current_height = -heap[0][0]

            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result
