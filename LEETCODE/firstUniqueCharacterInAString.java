class Solution {
    public int firstUniqChar(String s) {
        // Read the question wrong, this is incomplete
        char firstLetter = s.charAt(0);
        if (s.length() == 1) return 0;
        int index = 1;
        while (index < s.length()){
            if (s.charAt(index) != firstLetter) return index
        }
    }
}