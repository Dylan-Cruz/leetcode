# Write Up

## Approach

The low hanging fruit here is you can solve this in O(N^2) time by iterating with a nested loop to scan for each numbers compliment in regards to the target.

The follow up question suggests better is possible.

By using a hashmap of value to the index it appeared, you can check as we iterate if we've encountered the compliment of the current value previously in the list. If so, we can return.

## Time Complexity

- O(N)
- Every element is visited in the event the two values are the last two elements in the list

## Space Complexity

- O(N)
- A dictionary is instantiated to track where each value encountered so far is located that can grow to N size
