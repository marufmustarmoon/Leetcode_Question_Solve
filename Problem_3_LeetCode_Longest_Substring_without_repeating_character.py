def lengthOfLongestSubstring(s: str) -> int:
    longest = {}
    start = 0
    length = 0
    for end in range(len(s)):
        char = s[end]
        
        if char in longest and longest[char] >= start:
            start = longest[char] + 1
        
        longest[char] = end   
        
        length = max(length, end - start + 1)
    
    return length


s = "pwwkew"
result = lengthOfLongestSubstring(s)
print(result)  
