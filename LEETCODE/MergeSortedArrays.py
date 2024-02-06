class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Clone = nums1.copy() # deep copy nums1, use this to read from list without it being overwritten
        pointer1 = 0 # pointer to read nums1 clone
        pointer2 = 0 # pointer to read nums2
        for i in range(m + n):# i is the pointer to write into nums 1
            if pointer1 >= m: # if pointer1 exceeds limit (cant be larger than size of list)
                nums1[i] = nums2[pointer2] # put in the rest of nums2 into nums1
                pointer2 += 1
            elif pointer2 >= n: # if pointer2 exceeds limit
                nums1[i] = nums1Clone[pointer1] # put in the rest of nums1 clone into nums1
                pointer1 += 1
            elif nums1Clone[pointer1] < nums2[pointer2]: # basic logic of reading list and adding into nums1
                nums1[i] = nums1Clone[pointer1]
                pointer1 += 1
            else: # other basic logic
                nums1[i] = nums2[pointer2]
                pointer2 += 1
