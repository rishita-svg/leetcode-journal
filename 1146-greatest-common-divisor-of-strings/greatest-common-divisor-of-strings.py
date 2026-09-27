class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small = min(len(str1), len(str2))

        for i in range(small, 0, -1):
            x = str1[:i]

            if len(str1) % i == 0 and len(str2) % i == 0:
                if x * (len(str1) // i) == str1 and x * (len(str2) // i) == str2:
                    return x

        return ""