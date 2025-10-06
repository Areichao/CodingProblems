public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int counter = 0;
        int backCounter = nums.Length;
        while (counter < backCounter){
            if (nums[counter] == val){
                backCounter--;
                nums[counter] = nums[backCounter];
            }
            else counter++;
        }
        return counter;
    }
}