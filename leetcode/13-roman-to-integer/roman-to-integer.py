class Solution:
    def romanToInt(self, s: str) -> int:

        standard = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        special = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        sum = 0

        # Iterate over all characters in s
        for i in range(0, len(s)):

            # Special case previous
            if i > 0 and s[i-1: i+1] in special:
                continue

            # Special case
            if s[i: i+2] in special:
                sum += special[s[i: i+2]]
                continue

            sum += standard[s[i]]

        return sum


solution = Solution()
print(solution.romanToInt("III"))       # 3
print(solution.romanToInt("IV"))        # 4
print(solution.romanToInt("IX"))        # 9
print(solution.romanToInt("LVIII"))     # 58
print(solution.romanToInt("MCMXCIV"))   # 4
