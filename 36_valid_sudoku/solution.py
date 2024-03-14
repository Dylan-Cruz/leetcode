from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make containers to hold
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # add values from the matrix as we iterate
        # if a value already exists in the set, return false
        for i in range(9):
            row = board[i]
            for k in range(9):
                cell = row[k]

                if cell != ".":
                    # check if we've encountered this number in any row, col, or square
                    if cell in rows[i] or cell in cols[k] or squares[(i // 3, k // 3)]:
                        return False

                    # add our value to the associated sets
                    rows[i].add(cell)
                    cols[k].add(cell)
                    squares[(i // 3, k // 3)].add(cell)

        return True


# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]

board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]

solution = Solution()
print(solution.isValidSudoku(board))
