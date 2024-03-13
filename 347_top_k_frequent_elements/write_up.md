# Write Up

## Approach
### Initial Solution
Instinctually I knew I was far away from the optimal solution but after a reasonable amount of time I went ahead and implmemented it anyways. The worflow was to count the frequency of the elements, put them into a list, and sort it. This would simplify to a runtime complexity of O(N^2 * logn). Usually exponential runtime is an indicator this can be done faster.

If this were in Java where I was more at home with the libraries I'd have probably added the frequency of each element to a priority queue and then popped the highest ones off the queue.

After realizing there was a lot of room to improve I looked at some other solutions. A common optimization on what I had implemented was to use the counter, nix the sort, and then iterate over the counter items keeping a list of the top k frequencies. 

I also saw that the counter object has a method signature similar to a dictionary so I could use the optimized counter library instead of writing my own implementation with a defaultdict. Continuing on with the counter object interface I learned that there's a built in method to handle this exact problem implemented with a heap queue (priority queue). The implementation of these methods have a runtime complexity of O(N log K)

### Optimal Solution
Ultimately none of these solutions are optimal. This problem can be solved in linear time using a modified bucket sort approach thanks to the input constraints. You still have to count the frequencies but then you add them to a list. Each index of the list represents a possible frequency. Then you iterate over the frequencies putting them into their correct position (bucket) in the list. From there you can iterate backwards until you reach k frequencies. 

## Time Complexity

## Space Complexity
