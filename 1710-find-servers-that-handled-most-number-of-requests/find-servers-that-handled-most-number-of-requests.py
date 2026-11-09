class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        count = [0] * k
        busy = []
        available = SortedList(range(k))
        
        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            
            if not available:
                continue
            
            target = i % k
            idx = available.bisect_left(target)
            
            if idx == len(available):
                idx = 0
            
            server_id = available[idx]
            available.remove(server_id)
            
            heapq.heappush(busy, (arrival[i] + load[i], server_id))
            count[server_id] += 1
        
        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count]