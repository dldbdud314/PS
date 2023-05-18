"""
3. Longest Substring Without Repeating Characters
- two pointers .. ing ..
"""


def lengthOfLongestSubstring(s: str) -> int:
    if not s: return 0

    lp, rp = 0, 0
    dic = {s[0]}
    max_len = 1
    while True:
        try:
            while lp < rp and s[rp + 1] in dic:
                dic.remove(s[lp])
                lp += 1
            rp += 1
            dic.add(s[rp])
            max_len = max(max_len, len(dic))

        except: break

    return max_len


print(lengthOfLongestSubstring("dvdf"))
