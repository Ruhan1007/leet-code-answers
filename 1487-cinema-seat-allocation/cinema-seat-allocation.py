class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[int]) -> int:
        rows = {}
        for row, seat in reservedSeats:
            rows.setdefault(row, set()).add(seat)
        
        result = (n - len(rows)) * 2
        
        for seats in rows.values():
            left = not (2 in seats or 3 in seats or 4 in seats or 5 in seats)
            mid = not (4 in seats or 5 in seats or 6 in seats or 7 in seats)
            right = not (6 in seats or 7 in seats or 8 in seats or 9 in seats)
            
            if left and right:
                result += 2
            elif left or mid or right:
                result += 1
        
        return result