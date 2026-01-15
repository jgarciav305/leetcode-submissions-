""""
The problem asks us to return ONLY ALL the vowels of an input string, leaving the non vowels how they were and returning a newly modified string
Approach: I scan once to collect vowels, reverse them, then scan again to put them back
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        vowelsFirst = ""

        # Looping through every letter within the input string
        for char in s:
            # If that particular index is a vowel append it
            if char in vowels:
                vowelsFirst += char

            # Captured the vowels and reversed them
            reversedVowels = vowelsFirst[::-1]

            # Reconstruct the original string 
            result = []
            vowelIndex = 0

        for char in s:
            if char in vowels:
                result.append(reversedVowels[vowelIndex])
                vowelIndex += 1
            else:
                result.append(char)

        return "".join(result)