using System.Collections.Specialized;

public class Solution {
    public int FirstUniqChar(string s) {
        OrderedDictionary<char, int> dict = new OrderedDictionary<char, int>();
        for (int i = 0; i < s.Length; i++){
            if (!dict.ContainsKey(s[i])) dict[s[i]] = 1;
            else dict[s[i]]++;
        }
        foreach (char key in dict){
            if (dict[key] == 1) return 
        }
    }
}