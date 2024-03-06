public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int, int> storage = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++){
            if (storage.ContainsKey(nums[i])){ return true;}
            storage.Add(nums[i], 0);
        }
        return false;
    }
}