# Write Up

## Approach

While there are certainly some ways to approach this problem involving converting the linked lists into numbers, doing addition, and putting the result into a new linked list, it's very apparent that you can do this mostly in place. The approach I came to was to iterate over both lists at the same time and add the sum of the two values for this place value together. The only thing to watch out for here was if the sum is more than 10, ensuring we carry over a 1 to the next place value evaluation. There are also a few fancy tricks to cut down on operations and conditionals I employed to get runtime down. Returning `result.next` was a big one since initializing `result` outside of the loop saved a comparison on every loop to check if it had been intialized.

## Time Complexity

- Time Complexity: O(N)
- Every element is visited once

## Space Complexity

- Space Complexity: O(N)
- A dictionary of size N is made to store the result
