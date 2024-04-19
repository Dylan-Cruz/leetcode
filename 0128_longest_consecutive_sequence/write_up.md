# Write Up

## Approach
This problem could easily be handled by sorting the array and checking for the longest sequence but leetcode challenges me to find a solution in O(N) time. My first theory is that if I add the elements to a set, for each key in the set, I can check if it has the next number to determine if they form a sequence. Here's where I got stuck. I didn't spend enough time thinking about where to go from there. Realistically I was realizing the fact that the lack of a left neighbor existing in a set means that that number is the start of a sequence away from solving this one. I think going forward I need to find paths one step at a time. I had the set and neighbor part down but didn't iterate from there when a solution didn't immediately present itself. 
## Time Complexity
- O(N)
- Each number in the list is visited at most twice as we iterate. Once to see if it's the start of a set, and as we traverse the length of the sequence. We also create a set from a list which is also N time. 
## Space Complexity
- O(N) 
- We had to create a set to reference as we iterated