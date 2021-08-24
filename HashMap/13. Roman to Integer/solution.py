class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        
        result = 0
        idx = len(s) - 1
        while idx != -1:
            if idx > 0 and s[idx - 1:idx + 1] in roman_mapping:
                result += roman_mapping[s[idx - 1:idx + 1]]
                idx -= 2
            else:
                result += roman_mapping[s[idx]]
                idx -= 1
        return result
        
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        
        result, prev = 0, 0
        idx = len(s) - 1
        while idx != -1:
            next_num = roman_mapping[s[idx]]
            if next_num < prev:
                result -= next_num
            else:
                result += next_num
            prev = next_num
            idx -= 1
        return result
        
