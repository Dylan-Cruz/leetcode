# Write Up

## Approach

My initial instinct was pretty close on this one. It was to count the number of primes in the range (NP) and return NP!. The only problem is, that only generates the permutations of prime numbers in prime indices. It doesn't consider the arrangement of nonprime numbers. To include those, we multiply NP! by C! where C is the number of composite numbers

## Time Complexity

O(N^2) since there's an inner loop in isPrime. This however is bound by a function that can be calculated

## Space Complexity

O(1) this is done in constant space
