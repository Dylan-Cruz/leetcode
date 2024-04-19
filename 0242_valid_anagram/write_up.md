# Write Up

I ended up with three solutions to this problem although there are likely more.

## Solution 1 - Dictionary Inventory

### Approach

I started with the idea that I could iterate over the first string storing an inventory of letter appearances in a dictionary. Then as I iterate over the second string I could pull letter appearances out of inventory. If we encountered a letter that wasn't present in the inventory, we could return False. Otherwise if we make it to the end, if any keys remain in the dictionary we could return false. Otherwise, there are no keys left meaning the two strings are anagrams.

This ended up with a slow runtime in comparison to other submitters, so with room to improve I kept searching for a faster solution.

### Time Complexity

- O(N)
- Since we iterate over both strings, runtime efficiency is O(N + M) but it simplifies down to O(N).

### Space Complexity

- O(N)
- A dictionary is instantiated to keep a count of letter occurrances

## Solution 2 - Array Inventory

### Approach

The follow up question stood out to me. It mentioned solving this if unicode characters were present. That made me realize I could likely use some math with the output of the ord() function to come to a more efficient solution.

I also noticed we could easily do the inventory in one loop iteration that accesses both strings. String 1 would add appearances and string 2 would remove them in each iteration. This looked like it would cut down runtime by half.

I started to implement this but then quickly realized that when iterating, as we decrement, we can't guarantee we've encountered that letter before. This meant that we'd have to store a position for every letter allowed in the input. It also meant that to be able to return we'd have to iterate over every element in the inventory to check if it was not 0. This would add m operations where m is the character range of the input.

I chose to go with a list of length 26 to track inventory where each element is initialized to 0. The element at index i would be the frequency of the letter with i distance from 'a'. This approach allowed memory use to be cut since lists are lighter than dictionaries.

### Time Complexity

- O(N)
- Technically the same big O efficiency as the first approach albeit slightly slower since you can't return early during the second loop checking the inventory.

### Space Complexity

- O(N)
- It's also technically the same space efficiency except in practice a list is lighter than a dictionary.

## Solution 3 - Counter

### Approach

Solution 2 yielded a slight drop in performance but a significant improvement in memory usage. Despite this, my submission still fell short of the top so I checked to see what I could be doing differently. It was here that I learned that python has a Counter object in the collections library that handles this exact problem. For any iterable the Counter will scan and record the frequency of each object. The solution using Counter was also only one line!!

I tested it out and was shocked to see that my runtime was significantly higher than an instance of the exact same subission. I did notice that in my solution I imported Counter from collections but theirs omitted that line. I tried the same and the code ran which is quite misleading. My guess is the leetcode test authors must import the collections library for something else making Counter available for free. Regardless, learning about the Counter object will certainly pay dividends as I continue to learn python.

### Time Complexity

- likely O(N)

### Space Complexity

- likely O(N)

Without diving into the implementation of Counter and knowing that the interface is very similar to that of a dictionary, it should be safe to say that it uses a dictionary under the hood. Therefore, this would still be O(N) efficiency and space. The gains in performance and memory are likely due to optimized library code. It should be noted that when the import is present this solution slows considerably.
