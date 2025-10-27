class Solution {
    public int singleNumber(int[] nums) {
        // the XOR method lol. itll cancel out all duplicates regardless of order
        int single = 0;
        for(int i : nums) single ^= i;
        return single;
    }
}