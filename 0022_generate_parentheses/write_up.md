# Write Up

## Approach

## Time Complexity

## Space Complexity

# temp approach
1. generate a tree of all possibilities
    1. base case is length = n * 2 since n is the number of open parenthesis
    2. if stack size is n*2 add to return array
    3. at each position in the stack, you can either add an open or close parenthesis
    4. so each call of the method should spawn two calls. One where an open is added and one where a closing is added
    5. after each call the character added should get popped off the stack since 
2. then prune the tree with logic to exclude branches that won't generate valid answers

