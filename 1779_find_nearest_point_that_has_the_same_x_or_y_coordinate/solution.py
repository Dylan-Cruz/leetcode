from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        min_dist = float('inf')
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                dist = abs(x - point[0]) + abs(y - point[1])
                if dist < min_dist:
                    result = i
                    min_dist = dist
        
        return result
    
solution = Solution()
print(solution.nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))
print(solution.nearestValidPoint(3, 4, [[3,4]]))
print(solution.nearestValidPoint(3, 4, [[2,3]]))