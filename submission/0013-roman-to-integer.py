class Solution:
    def romanToInt(self, s: str) -> int:
        #solve a function that takes a string in roman numeras returns an integer
        #create a dictionary with the roman numerals and their values
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #create a variable to hold the sum of the roman numerals
        sum = 0
        #loop through the string
        for i in range(len(s)):
            #if the current index is less than the next index
            if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                #subtract the current index from the sum
                sum -= roman_numerals[s[i]]
            else:
                #add the current index to the sum
                sum += roman_numerals[s[i]]
        #return the sum
        return sum
