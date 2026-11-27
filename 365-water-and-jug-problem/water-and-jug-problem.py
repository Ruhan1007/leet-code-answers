class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        from math import gcd

        if target > x + y:
            return False

        return target % gcd(x, y) == 0
