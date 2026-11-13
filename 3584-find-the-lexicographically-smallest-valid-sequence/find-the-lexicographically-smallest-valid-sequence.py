from bisect import bisect_left
from collections import defaultdict

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        pos = defaultdict(list)
        for i, c in enumerate(word1):
            pos[c].append(i)

        right = [[-1] * 2 for _ in range(m + 1)]
        right[m] = [n, n]

        for j in range(m - 1, -1, -1):
            arr = pos[word2[j]]

            p = bisect_left(arr, right[j + 1][0]) - 1
            right[j][0] = arr[p] if p >= 0 else -1

            p = bisect_left(arr, right[j + 1][1]) - 1
            exact = arr[p] if p >= 0 else -1

            right[j][1] = max(exact, right[j + 1][0] - 1)

        ans = []
        idx = 0
        rem = 1

        for j in range(m):
            if idx < n and idx < right[j + 1][rem]:
                if word1[idx] == word2[j]:
                    ans.append(idx)
                    idx += 1
                    continue

                if rem > 0 and idx < right[j + 1][rem - 1]:
                    ans.append(idx)
                    idx += 1
                    rem -= 1
                    continue

            arr = pos[word2[j]]
            p = bisect_left(arr, idx)

            if p == len(arr) or arr[p] >= right[j + 1][rem]:
                return []

            idx = arr[p]
            ans.append(idx)
            idx += 1

        return ans