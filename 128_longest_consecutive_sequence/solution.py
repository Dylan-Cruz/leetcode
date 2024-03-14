from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put the numbers in a set
        num_set = set(nums)

        # make a value to return
        longest_sequence = 0

        # for each key
        for num in num_set:
            sequence_length = 0
            # check if it's the start of a sequence
            if num - 1 not in num_set:
                sequence_length += 1

                # if so, see how long the sequence runs
                next_num = num + 1
                while next_num in num_set:
                    sequence_length += 1
                    next_num += 1

                # check if it's longer than the current longest
                if sequence_length > longest_sequence:
                    longest_sequence = sequence_length

        # return the largest sequence encountered
        return longest_sequence


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
