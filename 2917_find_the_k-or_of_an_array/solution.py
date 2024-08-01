from typing import List
from collections import defaultdict

class Solution:
    def findKOr(self, nums: List[int], x: int) -> int:
        # for each int in the list
            # call bin
            # for each character (bit) in the string
                # bucket accumulate them
        # convert the array to a binary string
        # convert it back to an int
        arr = [0] * 31

        for i in nums:
            binary = bin(i)[:1:-1]
            for index, k in enumerate(binary):
                if k == '1':
                    arr[index] += 1
        
        result_binary = ''.join(['1' if k >= x else '0' for k in arr[::-1]])
        return int(result_binary, 2)


solution = Solution()
e1 = solution.findKOr([7,12,9,8,9,15], 4)
print(e1)
e2 = solution.findKOr([2,12,1,11,4,5], 6)
print(e2)
e3 = solution.findKOr([10,8,5,9,11,6,8], 1)
print(e3)
e4 = solution.findKOr([0], 1)
print(e4)
e5 = solution.findKOr([4], 1)
print(e5)

