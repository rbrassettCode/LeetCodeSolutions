class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        listWords = s.split()

        resultList = ''
        for word in listWords:
            resultList = resultList + " " + word[::-1]
        
        return resultList[1:]
        
'''
    1 -- seperate String of words into seperate string words
    2 -- iterate through list and reverse the word using reverse() function
    3 -- remove starting whitespace 
'''
    
solution = Solution()

result = solution.reverseWords("Let's take LeetCode contest")

print(result)