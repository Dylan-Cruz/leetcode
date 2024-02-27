from typing import List


class Solution:
    """
    This function determines if a duplicate entry exists
    in the list of nums

    Parameters:
    nums (List[int]): the list of numbers to scan

    Returns:
    boolean: True if a duplicate is found. False otherwise.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if not num in num_set:
                num_set.add(num)
            else:
                return True
        return False


# Tests
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
