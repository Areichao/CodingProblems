public class Solution {
    public int StrStr(string haystack, string needle) {
        // accidentally counted number of haystack, not first index
        // base case number 1 
        if (haystack.Length < needle.Length) return -1;
        int counter = 0;
        for (int index = 0; index + needle.Length <= haystack.Length; index++){
            if (haystack[index] == needle[0]){
                string substring = haystack.Substring(index, needle.Length);
                if (substring == needle) counter++;
            }
        }
        // return -1 if the counter is 0
        return (counter == 0) ? -1 : counter;

    }


    public int StrStr(string haystack, string needle) {
        // here should be the actual solution
        // base case number 1 
        if (haystack.Length < needle.Length) return -1;
        int counter = 0;
        for (int index = 0; index + needle.Length <= haystack.Length; index++){
            if (haystack[index] == needle[0]){
                string substring = haystack.Substring(index, needle.Length);
                if (substring == needle) return index;
            }
        }
        // return -1 if the counter is 0
        return -1;

    }
}