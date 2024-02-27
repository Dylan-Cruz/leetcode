# Write Up
## Approach
We can use a hash set to track if we've encountered a number previously as we iterate over the list. If the map contains the list element we're inspecting, there's a duplicate so we can return true. If we reach the end of the list without finding a duplicate, return false.
## Efficiency
The efficiency is O(N) since every element is visited in the event there are no duplicates. 