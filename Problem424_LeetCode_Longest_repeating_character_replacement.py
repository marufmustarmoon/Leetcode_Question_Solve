def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_len = 0
    max_freq = 0
    start = 0
    
    for end in range(len(s)):
        #use naive approach
        if s[end] in count:
            count[s[end]] += 1
        else:
            count[s[end]] = 1
        # use built in function get()
        # count[s[end]] = count.get(s[end], 0) + 1
        
       
        max_freq = max(max_freq, count[s[end]])
        
       
        if (end - start + 1) - max_freq > k:
           
            count[s[start]] -= 1
            start += 1
        
       
        max_len = max(max_len, end - start + 1)
    
    return max_len


s = "AABABBA"
k = 1

result = characterReplacement(s,k)
print(result)