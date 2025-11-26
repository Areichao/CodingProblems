class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = []
        originalWordlist = set(wordlist)
        allLower = {}
        allVowels = {}
        vowelsA = {"e", "i", "o", "u"}
        # populate the hash tables
        for word in wordlist:
            wordLower = word.lower()
            if wordLower not in allLower:
                allLower[wordLower] = word
            wordVowel = "".join("a" if v in vowelsA else v for v in wordLower)
            if wordVowel not in allVowels:
                allVowels[wordVowel] = word
        # iterate through query
        for q in queries:
            if q in originalWordlist:
                result.append(q)
            else:
                lower = q.lower()
                if lower in allLower:
                    result.append(allLower[lower])
                else:
                    vowels = "".join("a" if v in vowelsA else v for v in lower)
                    if vowels in allVowels:
                        result.append(allVowels[vowels])
                    else:
                        result.append("")
        return result

