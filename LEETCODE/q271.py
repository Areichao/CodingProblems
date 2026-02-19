class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}+{string}"
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        length = ""
        decoded = []
        while i < len(s):
            if s[i] != "+":
                length += s[i]
                i += 1
            else:
                decoded.append(s[i+1:i+int(length)+1])
                i += int(length) + 1
                length = ""
        return decoded



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))