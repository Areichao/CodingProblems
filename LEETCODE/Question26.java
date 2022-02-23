public class Question26 {
    public static void main(String[] args){
        int[] array = {0,0,1,1,1,2,2,3,3,4};
        System.out.println(removeDuplicates(array));
    }
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int removed = 0;
        int kept = 1;
        int previous = nums[0];
        for(int i = 1; i < nums.length; i++){
            if (nums[i] == previous){
                removed++;
            }
            else{
                previous = nums[i];
                nums[i-removed] = nums[i];
                kept++;
            }
        }
        return kept;
    }
}