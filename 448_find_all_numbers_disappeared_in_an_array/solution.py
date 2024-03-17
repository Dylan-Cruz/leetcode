from typing import List


class Solution:
    def findDisappearedNumbers_set(self, nums: List[int]) -> List[int]:
        return set(range(1, len(nums) + 1)) - set(nums)

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        # for each number, invert the number in it's expected spot in the array
        for n in nums:
            # get the abs of the value to look at the index it belongs in
            index = abs(n) - 1
            # if it's not negative, make it so
            if (nums[index] > 0):
                nums[index] = nums[index] * -1

        # iterate over the range and return a list containing the positive indexes
        return [i for i in range(1, len(nums)+1) if nums[i-1] > 0]
    
        
solution = Solution()
print(solution.findDisappearedNumbers([5, 3, 6, 3, 1, 3]))