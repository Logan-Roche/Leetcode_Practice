class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "/"
        else:
            return "/".join(strs)

    def decode(self, s: str) -> List[str]:
        decodedList = []
        previousIndex = 0
        
        if s == "":
            decodedList.append("")
        elif s == "/":
            return decodedList

        for i in range(len(s)):
            if s[i] == "/":
                decodedList.append(s[previousIndex:i])
                previousIndex = i + 1
            elif i == len(s) - 1:
                decodedList.append(s[previousIndex:i + 1])
        return decodedList

