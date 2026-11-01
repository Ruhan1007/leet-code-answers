
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on starting time
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:

            # If merged is empty or intervals don't overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                # Merge overlapping intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
