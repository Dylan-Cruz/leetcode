# Write Up

## Approach
This one is pretty easy. We enumerate over the list checking if the current index mod 10 is equal to the value at that spot in the array. Since the problem is looking for the smallest index, we can return as soon as it's found. Return -1 in the event none is found.

## Time Complexity
O(N) each node is visited in the worst case where no index mod 10 equals nums[index]

## Space Complexity
O(1) no additional space is utilized