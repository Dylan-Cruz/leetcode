from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = deque()

        for index, value in enumerate(temperatures[::-1]):
            if len(stack) == 0:
                stack.append([index, temperatures[index]])
            else:   
                top = stack[-1]
                if top[1] > temperatures[index]:
                    

        
        # if the next value in the array is greater than the value on the top of the stck
        # set the associated value in the arra to the difference.
        # otherwise push it on the stack as well
        # at the end of the array, push 0 to any remaining associated indexes

