class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # 0 or 10 11
        # go through array from left to right
        # if value is 0 point to next value
        # if value is 1 point to next value + 1
        # if pointer is length array - 1 then false otherwise true
        pointer = 0
        while pointer < len(bits) - 1:
            if bits[pointer] == 0:
                pointer += 1 
            else:
                pointer += 2
        return pointer == len(bits) - 1
