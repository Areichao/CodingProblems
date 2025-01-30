from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ group anagrams together """
        # create a default dictionary of lists as values
        anagramGroups = defaultdict(list)
        for word in strs:
            # sort the word into a list of characters
            chars = tuple(sorted(word))
            # if this key is in the dictionary (another word has the same letters) then append into values
            anagramGroups[chars].append(word)
        return list(anagramGroups.values())