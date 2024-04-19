# Write Up

## Approach
My first instinct here was to use two pointers to iterate over the linked list where the second moves twice as fast as the first. This allows us to complete the operation in one pass of the list. Alternatively you could solve this slightly less efficiently by counting the length of the list and iterating to the middle element.
## Time Complexity
- O(N) 
- Every node in the list is visited

## Space Complexity
- O(1)
- an additional pointer is used but it's still constant space
