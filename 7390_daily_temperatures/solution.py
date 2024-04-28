from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a monotonic decreasing stack 
        
        # if the next value in the array is greater than the value on the top of the stck
        # set the associated value in the arra to the difference.
        # otherwise push it on the stack as well
        # at the end of the array, push 0 to any remaining associated indexes