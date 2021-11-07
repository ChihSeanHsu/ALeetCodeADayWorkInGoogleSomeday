class Solution:
    def countVowels(self, word: str) -> int:
        vowel = "aeiou"
        result = 0
        prev = 0
        
        # "aba"
        for idx, c in enumerate(word):
            # a: prev = 1 result = 1
            # b: prev = 1 result = 2
            # a: prev = 1 + 1 (itself) + 2 (show in how many substrings) result = 6
            if c in vowel:
                prev += idx + 1 # this vowel will show in how many substrings and itself
            result += prev

        return result
