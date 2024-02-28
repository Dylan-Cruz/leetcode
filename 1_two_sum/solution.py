from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store each encountered element and it's index in a hashmap
        # as we iterate, check the map to see if we've encountered the compliment
        # if so, return the two indexes

        num_map = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if num_map.get(compliment) is not None:
                return [num_map.get(compliment), i]
            num_map[nums[i]] = i


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
