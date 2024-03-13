class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))

        i = len(digits) - 2
        while i>= 0 and digits[i] >= digits[i+1] :
            i -= 1
        
        if i == -1:
            return -1
        
        j = len(digits) - 1
        while j >= 0 and digits[j]<=digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]

        digits[i+1:] = reversed(digits[i+1:])

        result = int(''.join(digits))

        if result > 2**31 - 1:
            return -1
        
        return result


'''
    1 -- seperate int into list of str/chars
    2 -- find first decreasing digit from right to left using i
    3 -- a) if i reaches -1 it has no decreasing digit thus no solition 
         b) if i found first decreasing digit then we need to reorder digits to the right
    4 -- find first number smaller that i and switch that value and the i
    5 -- In order to get smallest possible greater element than we need to reverse the remaining ints
         to the right of our swapped character
    6 -- check for overflow of the int for large numbers
    7 -- return result in int format

'''

solution = Solution()
result = solution.nextGreaterElement(2318221)

print(result)