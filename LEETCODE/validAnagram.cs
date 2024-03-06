public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        Dictionary<char, int> letters = new Dictionary<char, int>();
        foreach (char letter in s){
            if (letters.ContainsKey(letter)) letters[letter] += 1;
            else letters.Add(letter, 1);
        }
        foreach (char letter in t){
            if (letters.ContainsKey(letter) && letters[letter] != 0) letters[letter] -= 1;
            else return false;
        }
        return true;
    } 
}