from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        rows = []
        col = []
        rowNum = 0
        for value in original:
            col.append(value)
            if len(col) == n:
                rows.append(col)
                col = []

        return rows
    
    def betterConstruct2DArray(self, original: List[int], m: int, n:int) -> List[List[int]]:
        array_2d = []
        if len(original) == m * n:
            for ind_row in range(m):
                array_2d.append(original[ind_row*n : ind_row*n + n])

        return array_2d      

    
solution = Solution()
print(solution.construct2DArray([6,2,6,1,8,9,1,2,6], 3, 3))
print(solution.construct2DArray([6,2,6,1,8,9,1,2], 3, 3))
print(solution.construct2DArray([1,2,3,4,5], 2, 2))
print(solution.construct2DArray([6,2,6], 1,3))