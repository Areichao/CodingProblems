from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ return the k most frequent element """
        numsCounter = Counter(nums) # Time complexity : O(n) Space Complexity: O(n)
        listKeys = [k for k in numsCounter.keys()] # Space Complexity: O(n)
        return sorted(listKeys, key = lambda num: numsCounter[num], reverse= True)[:k] # Time Complexity O(n log n)

# trying for time shorter than O(n log n)
# heapq.nsmallest(k, wordCount.keys(), key=lambda word: (-wordCount[word], word))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ return the k most frequent element """
        numsCounter = Counter(nums) # Time complexity : O(n) Space Complexity: O(n)
        return heapq.nlargest(k, numsCounter.keys(), key = lambda num: numsCounter[num]) # time Complexity can be O(n log K)
