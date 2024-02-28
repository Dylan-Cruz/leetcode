# Write Up
## Approach
We can use a hash set to track if we've encountered a number previously as we iterate over the list. If the map contains the list element we're inspecting, there's a duplicate so we can return true. If we reach the end of the list without finding a duplicate, return false.
## Time Complexity
- Time Complexity: O(N)  
- Every element is visited in the event there are no duplicates
## Space Complexity
- Space Complexity: O(N)  
- A dictionary of size N is made to check if we've encountered the current element before