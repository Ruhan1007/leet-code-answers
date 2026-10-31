MOD = 10**9 + 7

class Solution:
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        # place[r][c][d]: d=0 means RIGHT, d=1 means DOWN
        # result: (r', c') or (-1,-1) for invalid
        place = [[[None, None] for _ in range(n)] for _ in range(m)]
        # We'll fill for r+c from m+n-2 down to 0.
        # But simpler: compute on demand with iterative + memo, or just fill reverse order.
        # Since each transition goes to r+c+1, we can fill from high r+c to low.
        # Let's fill row-major reverse: r from m-1 down to 0, c from n-1 down to 0.
        # Does place[r][c][d] depend on place with same r+c or higher?
        # place at (r,c) mirror: DOWN -> (r,c+1) RIGHT [r+c+1], RIGHT -> (r+1,c) DOWN [r+c+1]. So depends on r+c+1.
        # Reverse row-major: we process r=m-1..0, c=n-1..0. When at (r,c), (r,c+1) is same r, larger c -> already processed (since c decreasing). (r+1,c) has larger r -> already processed. So reverse row-major works.
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                for d in (0,1):  # 0=RIGHT, 1=DOWN
                    if grid[r][c] == 0:
                        place[r][c][d] = (r,c)
                    else:
                        # mirror
                        if d == 1:  # entered moving DOWN -> turned RIGHT -> go to (r,c+1) moving RIGHT
                            if c+1 >= n:
                                place[r][c][d] = None
                            else:
                                place[r][c][d] = place[r][c+1][0]  # RIGHT
                        else:  # d==0, entered moving RIGHT -> turned DOWN -> go to (r+1,c) moving DOWN
                            if r+1 >= m:
                                place[r][c][d] = None
                            else:
                                place[r][c][d] = place[r+1][c][1]  # DOWN
        # Now dp
        dp = [[0]*n for _ in range(m)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if grid[r][c] == 1:
                    continue  # dp not used
                if r == m-1 and c == n-1:
                    dp[r][c] = 1
                    continue
                total = 0
                # try right
                if c+1 < n:
                    if grid[r][c+1] == 0:
                        total += dp[r][c+1]
                    else:
                        # mirror at (r,c+1), move right into it -> turned down -> (r+1,c+1) moving DOWN
                        if r+1 < m:
                            res = place[r+1][c+1][1]  # DOWN
                            if res is not None:
                                rr, cc = res
                                total += dp[rr][cc]
                # try down
                if r+1 < m:
                    if grid[r+1][c] == 0:
                        total += dp[r+1][c]
                    else:
                        # mirror at (r+1,c), move down into it -> turned right -> (r+1,c+1) moving RIGHT
                        if c+1 < n:
                            res = place[r+1][c+1][0]  # RIGHT
                            if res is not None:
                                rr, cc = res
                                total += dp[rr][cc]
                dp[r][c] = total % MOD
        return dp[0][0] % MOD