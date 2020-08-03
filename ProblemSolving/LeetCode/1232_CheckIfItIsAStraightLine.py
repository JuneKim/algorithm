class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        x1 = coordinates[1][0]
        y1 = coordinates[1][1]
        
        if x1 - x0 is not 0:
            dxdy0 = (y1 - y0)/(x1 - x0)
        else:
            dxdy0 = -1
        for x, y in coordinates[2:]:
            dx = x - x0
            dy = y - y0
            if dx is not 0:
                dydx = dy/dx
            else:
                dydx = -1
                
            if dydx != dxdy0:
                return False
        
        return True
