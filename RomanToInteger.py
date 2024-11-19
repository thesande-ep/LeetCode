def romanToInt(s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0
        for char in s[::-1]:
            cur_value = roman_map[char]
            if cur_value < prev_value:
                result = result - cur_value
            else:
                result = result + cur_value
            prev_value = cur_value
            prev_value = char
        return result, prev_value
        



print(romanToInt("VI"))