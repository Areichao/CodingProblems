class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # go through each one with the shorter word
        final = ""
        index = 0
        while index < len(word1) and index < len(word2):
            final += word1[index] + word2[index]
            index += 1
            if index == len(word1):
                final += word2[index:]
            elif index == len(word2):
                final += word1[index:]
        return final
