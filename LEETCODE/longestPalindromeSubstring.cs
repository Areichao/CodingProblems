public class Solution {
    public string LongestPalindrome(string s) {
        // create a 2d array of size n and fill it with boolean false
        int stringLength = s.Length;
        bool[,] dynamicArray = new bool[stringLength, stringLength];
        Array.Fill(dynamicArray, false);

        // store the starting and end index of palindrome here
        int[] palindrome = new int[2] {0, 0};

        for (int i = 0; i < stringLength; i++)
            dynamicArray[0, i] = true;

        
    }
}