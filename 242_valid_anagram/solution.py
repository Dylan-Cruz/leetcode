class Solution1:
    # runtime beats 86% of users
    # memory beats 56% of users
    def isAnagram(self, s: str, t: str) -> bool:
        # check if strings are different lengths
        if len(s) != len(t):
            return False
        
        # use hash map to store a record of the letters in a word
        # iterate over the candidate word pulling letters out
        # if any keys in the map are still present, return false
        letters = {}
        # do inventory on the letters
        for letter in s:
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1

        # remove letters in string t from inventory
        for letter in t:
            if letter in letters:
                if letters[letter] == 1:
                    letters.pop(letter)
                else:
                    letters[letter] = letters[letter] - 1
            else:
                return False

        # if the inventory map is empty, return true
        if len(letters.keys()) == 0:
            return True

solution1 = Solution1()
print(solution1.isAnagram("anagram", "nagaram"))
print(solution1.isAnagram("rat", "car"))

class Solution2:
    # runtime beats 83% of users
    # memory beats 79% of users
    def isAnagram(self, s: str, t: str) -> bool:
        # check if strings are different lengths
        if len(s) != len(t):
            return False
        
        # make a list 26 elements long initialized to 0
        letters = [0] * 26
        
        for i in range(len(s)):
            # for each letter in each string increment or decrement
            # the associated index of the array. values are stored 
            # in the index equal to their distance from 'a'
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1
        
        # check if any array index is less than 0
        for count in letters:
            if count < 0:
                return False
            
        return True

solution2 = Solution2()
print(solution2.isAnagram("anagram", "nagaram"))
print(solution2.isAnagram("rat", "car"))


from collections import Counter
class Solution3:
    # runtime beats 95% of users
    # memory beats 79% of users
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

solution3 = Solution3()
print(solution3.isAnagram("anagram", "nagaram"))
print(solution3.isAnagram("rat", "car"))
