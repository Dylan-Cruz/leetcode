# Write Up
## Approach
Initially this problem seemed pretty easy. Right off the bat you can brute force this in O(N^2) time. The problem statement requires O(N) and you can't use the division operator. Okay, this got a lot harder. My intuition said there's some way to culmulatively store products as we go but after about an hour I ultimately looked at a solution and analyzed it. 

First, to make sure the approach sunk in, I manually walked through the algorithm in a notebook for the input `[1,2,3,4]`. After that it was clear that you can iterate from beginning to end of the input array storing the product of all elements that come before the current element in it's adjacent position in the result array. After that iteration, you iterate from the end of the input array to the front doing the same thing. What you get is the product of all the elements in the input before the position times the product of all the elements after the position thus solving the problem. 

## Time Complexity
- O(N)  
- We iterate over the input list twice which is 2N and that simplies to O(N)
## Space Complexity
- O(N)   
- We use an additional N space for the result array 