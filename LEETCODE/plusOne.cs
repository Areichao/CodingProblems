public class Solution {
    public int[] PlusOne(int[] digits) {
        // length of digits
        int digitsLength = digits.Length;
        // iterate from the end of the array. 
        for (int i = digitsLength - 1; i >= 0; i --){
            // if digit is not 9, increment by one and return value
            if (digits[i] < 9){
                digits[i] += 1;
                return digits;
            }
            // else, if it is, change digit to 0 and continue loop
            digits[i] = 0;
        }
        // if it made it out of the loop, need to add a 1 at the front of array
        int[] newDigits = new int[digitsLength + 1];
        Array.Fill(newDigits, 0);
        newDigits[0] = 1;
        return newDigits;
    }
}