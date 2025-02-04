class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """ return the K most frequent words, if tied, lexiographically sort """
        wordCount = {} # sets word as key and value as how many times its appeared
        for w in words:
            wordCount.setdefault(w, 0)
            wordCount[w] += 1
        sortedWords = [wo for wo in wordCount.keys()]
        sortedWords.sort(key = lambda word: (-wordCount[word], word))
        return sortedWords[:k]
# can use heapq (priority queue) to sort faster in cases with small k value
# return heapq.nsmallest(k, wordCount.keys(), key=lambda word: (-wordCount[word], word))
