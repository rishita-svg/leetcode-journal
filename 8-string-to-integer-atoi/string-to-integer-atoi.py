class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        num = 0
        n = len(s)

        # 1. Skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # 4. Clamp range
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num   # ← THIS IS THE MOST IMPORTANT LINE
