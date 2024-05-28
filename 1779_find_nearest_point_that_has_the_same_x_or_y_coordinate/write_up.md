# Write Up

## Approach

This one was easy enough. Iterate through the list, if the point is valid, calculate the distance and see if it's the new minimum. If so, store the index to return. You can gain some speed by initializing the starting minimum to positive infinity instead of None which will eliminate a comparison on every element of the points list. Use the enumerate loop to be more concise and pythonic.

## Time Complexity

O(N) since each element in the list is visited once

## Space Complexity

O(1) since no additional collections are needed
