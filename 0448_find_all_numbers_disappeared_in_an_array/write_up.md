# Write Up

## Approach
The easiest approach to this one is of course to utilize the set library. You can very easily add the range of expected integers to a set, add the passed list to a set, and then get the difference. Leetcode however challenges us to do this in space with the caveat that the array to be returned isn't considered used space. I ended up getting pretty close but was unable to come to a solution with this complexity on my own. I needed to consider mutating the array passed in in order to get there which so far has been a divergence from how I've approached problems. The in place, linear approach is to loop over the nums array and for each number we encounter invert the index in num to the negative number. This will mark encountered indexes with negative numbers leaving us to only iterate one more time collecting indexes with positive numbers into the result array. 
## Time Complexity
- O(N) 
- In both approaches the time complexity simplifies to O(N). 
- In the set approach, making each set is N ops since the range is the same length as the input array. This is done twice. Then a set lookup is O(1) for each element to calculate the diff. 
- In the in space approach you iterate at most twice.
## Space Complexity
- O(N) / O(1)
- The set approach uses linear extra space due to utilizing sets. 
- The in space approach uses the input array to track the elements that are present so uses constant space. 