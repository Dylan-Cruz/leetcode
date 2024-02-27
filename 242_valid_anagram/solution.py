class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
