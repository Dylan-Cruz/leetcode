# Write Up

## Instinct

My first instinct was to iterate over the list of strings and use a Counter object as a key to a list of strings that match the same counter signature.

## Approach

I wrote the Counter solution and got an error explaining that Counter isn't a hashable object in python because it's mutable. This was an approach I would use in Java since everything is hashable, you just have to know you won't mutate that object in the lifespan in which you'd use the hash table.

Since that approach didn't work, the next best bet I could think of was for each string, to sort a copy of it, and use that as the key. This approach worked just as well. Taking this approach exposed that I didn't know how to sort a string in python and that I didn't know much about the dict library as I originally built the return value with a loop.

My solution performed pretty well once written, beating 84% of submissions in runtime and 89% of submissions in memory usage. By investigating better solutions I learned I could optimize mine by using a defaultdict which uses a factory to initialize missing keys to a default value. This would allow me to remove my if statement and speed up my solution.

## Time Complexity

- O(N _ K _ logK) where n is the number of strings and k is the longest string in the list.
- This is derived from the sort call on the string k which is K logK performance being done N times.

## Space Complexity

- O(N \* K)
- We store a map to return of sorted strings K to lists of strings N strings in total length.
