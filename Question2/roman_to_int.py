import re
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = 0
        singles = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        couples = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        for item in couples:
            if re.search(item , s):
                roman_value += couples[item]
                s = s.replace(item, '')
        for part in s:
            roman_value += singles[part]
        return roman_value
        
if __name__ == "__main__":
    roman_number = input("Enter a Roman Number: ")
    print(Solution().romanToInt(roman_number))
        