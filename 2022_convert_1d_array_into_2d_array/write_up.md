# Write Up

## Approach

This one is easy enough although it'd be nice if python had a built in 2d array like Java. My initial and less efficient approach was to iterate over the list appending to a running column. If the running column is length N long, append the column to the rows list and make a new column. I forgot that python has array slicing, so there's a faster solution where you iterate over the numbers from 0 to m-1 and append a calculated slice from the orignal list.

## Time Complexity

Both run in O(N) time but the slicing method is faster as there's no check to see if we need to append and clear the column.

## Space Complexity

O(1) space since the return value doesn't count towards space complexity
