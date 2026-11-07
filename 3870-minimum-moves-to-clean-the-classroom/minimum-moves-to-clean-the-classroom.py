class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total = (1 << len(litter)) - 1

        if total == 0:
            return 0

        q = deque([(start[0], start[1], energy, 0, 0)])
        best = {}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c, e, mask, steps = q.popleft()

            if mask == total:
                return steps

            key = (r, c, mask)

            if best.get(key, -1) >= e:
                continue

            best[key] = e

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                cell = classroom[nr][nc]

                if cell == 'X':
                    continue

                ne = e - 1
                if cell == 'R':
                    ne = energy

                nmask = mask

                if cell == 'L':
                    nmask |= 1 << litter[(nr, nc)]

                q.append((nr, nc, ne, nmask, steps + 1))

        return -1
