class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []

        for j, task in enumerate(tasks):
            while busy and busy[0][0] <= j:
                time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            if not free:
                time = busy[0][0]

                while busy and busy[0][0] == time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)
            ans.append(idx)

            heapq.heappush(busy, (max(j, time if 'time' in locals() else j) + task, weight, idx))

        return ans
