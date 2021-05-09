class Solution:
    from math import sqrt
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        l,r = int(sqrt(L)), int(sqrt(R))
        # because there is only 10 ** 8
        MAGIC = 100000

        def is_palindrome(x):
            return x == x[::-1]

        ans = 0
        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(str(v)):
                ans += 1
        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(str(v)):
                ans += 1
        return ans
