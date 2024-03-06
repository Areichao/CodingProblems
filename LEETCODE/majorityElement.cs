public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int, int> track = new Dictionary<int, int>();
        int length = nums.Length / 2;
        for (int i = 0; i < nums.Length; i++){
            if (!track.ContainsKey(nums[i])) track[nums[i]] = 1;
            else track[nums[i]]++;
            if (track[nums[i]] > length) return nums[i];
        }
        return 1;
    }
}