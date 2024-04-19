from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result

    def productExceptSelfWithOutput(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            print(f"\n#### iteration {i+1}: i = {i} ####")
            print("# updating result")
            print(f"result[{i}] = {result[i]}")
            print(f"prefix_product = {prefix_product}")
            print(
                f"result[{i}] = {result[i]} * {prefix_product} = {result[i] * prefix_product}"
            )
            result[i] *= prefix_product
            print(f"result: {result}")
            print("# updating prefix product")
            print(
                f"prefix_product *= nums[i]: {prefix_product} *= {nums[i]} = {prefix_product * nums[i]}"
            )
            prefix_product *= nums[i]

        # Calculate suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            print(f"\n#### iteration {i+1}: i = {i} ####")
            print("# updating result")
            print(f"result[{i}] = {result[i]}")
            print(f"suffix_product = {suffix_product}")
            print(
                f"result[{i}] = {result[i]} * {suffix_product} = {result[i] * suffix_product}"
            )
            result[i] *= suffix_product
            print(f"result: {result}")
            print("# updating suffix product")
            print(
                f"suffix_product *= nums[i]: {suffix_product} *= {nums[i]} = {suffix_product * nums[i]}"
            )
            suffix_product *= nums[i]

        print(f"final result: {result}")
        return result


solution = Solution()
solution.productExceptSelfWithOutput([1, 2, 3, 4, 5])
