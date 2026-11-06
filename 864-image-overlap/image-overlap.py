class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        
        from collections import Counter
        shifts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shifts[(r1 - r2, c1 - c2)] += 1
        
        return max(shifts.values()) if shifts else 0