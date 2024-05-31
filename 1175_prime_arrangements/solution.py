class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # count the number of prime numbers 2 to n
        # there are the same number of prime indexes in a 1 indexed list 
        # accumulate n! as we encounter primes
        
