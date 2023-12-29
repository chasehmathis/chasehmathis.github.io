class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = []
        for i, s in enumerate(strs):
            new_s = s + '<sep>'
            if i == len(strs) - 1:
                new_s = s
            ret.append(new_s)
        return ''.join(ret)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        return s.split('<sep>')


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
