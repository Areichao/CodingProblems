class Solution:
    def expand(self, s: str) -> List[str]:
        # "{a,b}c{d,e}f"
        # change it into [[a, b], [c], [d, e], [f]]
        final_result = []
        letter_options = []
        inside_bracket = False
        inside_options = []
        for letter in s:
            if letter == "{":
                inside_bracket = True
            elif letter == "}":
                inside_bracket = False
                inside_options.sort() # sort it lexiographically first
                letter_options.append(inside_options)
                inside_options = []
            elif "a" <= letter <= "z" and not inside_bracket:
                letter_options.append([letter])
            elif "a" <= letter <= "z" and inside_bracket:
                inside_options.append(letter)

        self._recurse_letters(letter_options, final_result, "")
        return final_result
        
    # now use this to generate every option
    # change [[a, b], [c], [d, e], [f]] into ["acdf","acef","bcdf","bcef"]
    def _recurse_letters(self, letterArray: List[List[str]], final_output: List[str], current: str):
        # base case -> if list is empty, add to final output and return
        if len(letterArray) == 0:
            final_output.append(current)
            return

        # recursive case
        for letter in letterArray[0]:
            self._recurse_letters(letterArray[1:], final_output, current + letter)
