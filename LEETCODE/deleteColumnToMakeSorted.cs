public class Solution {
    public int MinDeletionSize(string[] strs) {
        // initiate a counter and set a reference previous as a character array, as strings are immutable
        int counter = 0;
        char[] previous = strs[0].ToCharArray();
        Dictionary<int, int> cancelled = new Dictionary<int, int>();
        // iterate through every element in array
        for (int i = 1; i < strs.Length; i++){
            // iterate though every letter in element
            for (int j = 0; j < strs[0].Length; j++){
                // if compareto value is less than or equal to 0, the lexiographic value is smaller (comes before) or the same. so add counter if this is NOT the case
                if (!cancelled.ContainsKey(j) && !(previous[j].CompareTo(strs[i][j]) <= 0)){
                    counter += 1;
                    cancelled.Add(j, 0); // make sure to not count column j again
                } 
                // set new previous value to current value
                previous[j] = strs[i][j];
            }
        }
        return counter;
    }

    /* 
    This function is the second faster attempt
    */
    public int MinDeletionSize(string[] strs) {
        int counter = 0;
        // go down each column first rather than row for earlier solution
        for (int i = 0; i < strs[0].Length; i++){
            for (int j = 1; j < strs.Length; j++){
                if (!(strs[j-1][i].CompareTo(strs[j][i]) <= 0)){
                    counter += 1;
                    break;
                }
            }
        }
        return counter;
    }
}