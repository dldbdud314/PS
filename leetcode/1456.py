"""
1456. Maximum Number of Vowels in a Substring of Given Length
- sliding window
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(c):
            return c in 'aeiou'

        l, r = 0, k - 1
        cnt = 0
        for i in range(l, r + 1):
            if is_vowel(s[i]):
                cnt += 1

        max_cnt = -1
        while r < len(s):
            if max_cnt > -1 and is_vowel(s[r]):
                cnt += 1

            if cnt > max_cnt:
                max_cnt = cnt

            if is_vowel(s[l]):
                cnt -= 1
            l += 1
            r += 1

        return max_cnt
