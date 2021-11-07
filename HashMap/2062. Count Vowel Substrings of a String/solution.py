class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        self.result = 0
        vowel = "aeiou"
        
        def helper(wo, met_vowel):
            if not wo or wo[0] not in vowel:
                return
            
            if wo[0] in vowel:
                met_vowel.add(wo[0])
                if len(met_vowel) == 5:
                    self.result += 1
                helper(wo[1:], met_vowel)
        
        
        for idx in range(len(word)):
            helper(word[idx:], set())
            
        return self.result
        
        
