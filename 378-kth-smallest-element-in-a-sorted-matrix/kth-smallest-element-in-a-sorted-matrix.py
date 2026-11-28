class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq

        n = len(matrix)
        heap = []

        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k - 1):
            val, row, col = heapq.heappop(heap)

            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return heapq.heappop(heap)[0]