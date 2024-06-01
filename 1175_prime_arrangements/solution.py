import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        encountered_primes = 0

        for i in range(2, n+1):
            if Solution.isPrime(i):
                encountered_primes += 1

        return math.factorial(n - encountered_primes) * math.factorial(encountered_primes) % (10**9+7)

    @staticmethod
    def isPrime(n):
        if n < 2:
            return False
        if n == 2: 
            return True
        if n % 2 == 0:
            return False
        
        for i in range(3, math.ceil(n**0.5) +1, 2):
            if n % i == 0:
                return False
        
        return True

solution = Solution()
print(solution.numPrimeArrangements(100))