class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            self.empty = True
        else:
            self.empty = False
        return "-".join(strs)

    def decode(self, s: str) -> List[str]:
        return [] if self.empty else s.split("-")
        