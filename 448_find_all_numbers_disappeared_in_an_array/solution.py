from typing import List


class Solution:
    def findDisappearedNumbers_set(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        