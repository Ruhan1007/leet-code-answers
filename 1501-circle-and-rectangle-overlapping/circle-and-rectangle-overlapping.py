class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find closest point on rectangle to circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Compare squared distance to squared radius (avoids sqrt)
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        
        return dx * dx + dy * dy <= radius * radius