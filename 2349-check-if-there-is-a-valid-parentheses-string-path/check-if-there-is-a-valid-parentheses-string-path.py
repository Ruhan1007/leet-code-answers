class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        visited = set()
        queue = deque([(0, 0, 0)])
        visited.add((0, 0, 0))

        while queue:
            i, j, bal = queue.popleft()
            bal += 1 if grid[i][j] == '(' else -1

            if bal < 0:
                continue

            remaining = (m - 1 - i) + (n - 1 - j)
            if bal > remaining:
                continue

            if i == m - 1 and j == n - 1:
                if bal == 0:
                    return True
                continue

            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i + di, j + dj
                if ni < m and nj < n:
                    state = (ni, nj, bal)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

        return False