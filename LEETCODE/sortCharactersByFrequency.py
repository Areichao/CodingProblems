from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        return "".join(sorted(s, key = lambda i: (-frequency[i], i)))


# a faster approach would be to use bucket sort, since there are a limited number of character (potential things to sort)
"""
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count character frequencies (O(n))
        frequency = Counter(s)
        
        # Step 2: Create a list of empty buckets (index = frequency count)
        max_freq = max(frequency.values())  # Find the highest frequency
        buckets = [[] for _ in range(max_freq + 1)]  # O(n) space
        
        # Step 3: Place characters into corresponding frequency buckets (O(n))
        for char, freq in frequency.items():
            buckets[freq].append(char)
        
        # Step 4: Build the output string from highest to lowest frequency (O(n))
        result = []
        for freq in range(max_freq, 0, -1):  # Traverse buckets in descending order
            for char in buckets[freq]:
                result.append(char * freq)  # Append char `freq` times
        
        return "".join(result)  # Convert list to string (O(n))
"""