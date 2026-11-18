class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total = s.count('1')

        starts = []
        ends = []

        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j + 1 < n and s[j + 1] == '1':
                    j += 1
                starts.append(i)
                ends.append(j)
                i = j + 1
            else:
                i += 1

        m = len(starts)

        if m == 0:
            return [0] * len(queries)

        size = 1
        while size < m:
            size *= 2

        seg = [0] * (2 * size)

        for i in range(m):
            left = starts[i] - ends[i - 1] - 1 if i > 0 else 0
            right = starts[i + 1] - ends[i] - 1 if i + 1 < m else 0
            seg[size + i] = left + right

        for i in range(size - 1, 0, -1):
            seg[i] = max(seg[2 * i], seg[2 * i + 1])

        def range_max(l, r):
            res = 0
            l += size
            r += size

            while l < r:
                if l & 1:
                    res = max(res, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = max(res, seg[r])
                l //= 2
                r //= 2

            return res

        from bisect import bisect_left, bisect_right

        ans = []

        for l, r in queries:
            first = bisect_left(ends, l)
            last = bisect_right(starts, r) - 1

            best = 0

            if first <= last:
                if first == last:
                    if starts[first] > l and ends[first] < r:
                        best = starts[first] - l + r - ends[first]

                else:
                    if starts[first] > l:
                        gain = starts[first] - l
                        gain += starts[first + 1] - ends[first] - 1
                        best = max(best, gain)

                    if ends[last] < r:
                        gain = starts[last] - ends[last - 1] - 1
                        gain += r - ends[last]
                        best = max(best, gain)

                    if first + 1 < last:
                        best = max(
                            best,
                            range_max(first + 1, last)
                        )

            ans.append(total + best)

        return ans