# Write Up

## Approach

There's two solutions to this that are relatively close. The key to this problem is that the minimum value when you push a new element will be the minimum value at that point in time if elements get popped off to make it the top again. With that in mind you can either define a second stack to maintain the minimum at the time of pushing a new element or you can use a single stack and push a tuple of val and min. I opted for the tuple route since there's less references.

## Time Complexity

- all methods in the min stack implementation run in O(1) time.

## Space Complexity

- a stack is O(N) space where N is the number of elements pushed.
