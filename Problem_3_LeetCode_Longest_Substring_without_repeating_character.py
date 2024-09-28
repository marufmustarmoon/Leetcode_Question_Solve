def lengthOfLongestSubstring(s: str) -> int:
    longest = {}
    start = 0
    length = 0
    for end in range(len(s)):
        char = s[end]
        if char not in longest:
            longest[char]=True
            length = max(length,end-start+1)

        else:
            while longest[char]:
                    longest[s[end]]=False
                    start= start + 1

            longest[s[end]]=True
    return length

s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(result)