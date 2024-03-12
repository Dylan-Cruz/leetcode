from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store the frequency of each unique element
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] = frequency_map[num] + 1

        # stream the key pairs into a list of tuples
        tuples = list(frequency_map.items())

        # sort the list and return the top k entries
        tuples.sort(key=lambda tup: tup[1], reverse=True)
        return [tup[0] for tup in tuples[:k]]


solution = Solution()
input = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print(solution.topKFrequent(input, 2))


# efficiency
# 2N * NlogN + k
# O(N^2 logN)

# memory
# 2N
# O(N)
