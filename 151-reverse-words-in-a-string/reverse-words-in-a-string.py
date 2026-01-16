""" 
Return the words in reverse order with just one space in between each word 
Approach: Split the words, reverse them and then join them together
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        y = x[::-1]
        z = z = " ".join(y)

        return z
          

        