class Solution:
    def romanToInt(self, s: str) -> int:
        # initialize a lookup table with roman values
        roman_lookup = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        # Setup variable
        sum = 0
        # loop through the s string
        for i in range(len(s)-1):
            if(roman_lookup[s[i]] < roman_lookup[s[i+1]]):
                sum -= roman_lookup[s[i]]
            else:
                sum += roman_lookup[s[i]]
        
        sum += roman_lookup[s[-1]]
        
        return sum


      
        
        