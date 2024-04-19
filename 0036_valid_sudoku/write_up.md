# Write Up

## Approach
My first instinct with this problem was to iterate over the matrix once, tracking all cells as we went in containers. Then at the end, validate that there was no overlap. While not entirely the most efficient, I was pretty close with my first take. Unfortunately though, I doubted that this was the optimal approach. I thought to myself "there has to be some trick" and talked myself out of the answer. 

After researching I realized that while there were some small ineficiencies with my solution, using lists instead of sets as containers, and returning early if possible, that I should've trusted my gut.

Ultimately the approach I found to be effective and optimal was to make dictionaries of sets to represent each row, column, and  square. Then as we iterate if the sets don't have this number already, add it to the respective container. I fun little trick I used was using a tuple of x,y (i,k in code) as the key for the squares. 

## Time Complexity
- O(1) 
- This runs in constant time since the input of a sudoku is bounded to 81 cells. 

## Space Complexity
- O(N) 
- We end up storing each cell in 3 different collections of buckets but it simplifies to linear space. 