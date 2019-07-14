class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if len(points) <= 1:
            return len(points)
        
        points = sorted(points, key=lambda element: (element[1]))
        print(points)
        
        arrows = 0
        currentSpot = points[0][0] - 1
        for point in points: 
            if currentSpot < point[0] or currentSpot > point[1]:
                arrows += 1
                currentSpot = point[1]
        return arrows
            
