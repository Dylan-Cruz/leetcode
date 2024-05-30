from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for index, val in enumerate(nums):
            if index % 10 == val:
                return index
        return -1
    
solution = Solution()
print(solution.smallestEqual([0,1,2]))
print(solution.smallestEqual([4,3,2,1]))
print(solution.smallestEqual([1,2,3,4,5,6,7,8,9,0]))