from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store the frequency of each unique element
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] = frequency_map[num] + 1

        # make a list of buckets and add the frequencies to their respective position
        buckets = [[] for _ in range(len(nums) + 1)]
        for c, v in frequency_map.items():
            buckets[v].append(c)

        # build our return value
        ret = []
        for bucket in reversed(buckets):
            for freq in bucket:
                if len(ret) < k:
                    ret.append(freq)

                if len(ret) == k:
                    return ret


solution = Solution()
data = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print(solution.topKFrequent(data, 2))
