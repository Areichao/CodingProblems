class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize length
        len_s1 = len(s1)
        len_s2 = len(s2)
        # if s1 is greater than s2, return false
        if len(s1) > len(s2):
            return False
        
        s1_letters, s2_sub = [0] * 26, [0] * 26
        # initialise array for s1, while also counting for first s2 window
        for i in range(len(s1)):
            index_s1 = ord(s1[i]) - ord('a')
            index_s2 = ord(s2[i]) - ord('a')
            s1_letters[index_s1] += 1
            s2_sub[index_s2] += 1
        
        # initialize pointer
        left = 0
        right = (left + len_s1) - 1
        # outer loop (while we can fit more windows)
        while right < len_s2:
            # get indexes of left and right
            index_l = ord(s2[left]) - ord('a')
            index_r = ord(s2[right]) - ord('a')
            # first loop, left = 0. check if it matches
            if left == 0:
                if s1_letters == s2_sub:
                    return True
            
            # otherwise, increment right index first, then check for match
            else:
                s2_sub[index_r] += 1
                if s1_letters == s2_sub:
                    return True
            
            # decrease left index and iterate
            s2_sub[index_l] -= 1
            left += 1
            right += 1
        return False


                