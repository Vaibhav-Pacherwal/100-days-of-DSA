## Sum of Beauty of All Substrings
def beauty(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    
    vals = list(freq.values())
    return max(vals)-min(vals)

def beautySum(s):
    sum,subStr = 0,""
    for i in range(len(s)):
        for j in range(i,len(s)):
            subStr += s[j]
            sum += beauty(subStr)
        subStr = ""
    
    return sum

s = "aabcb"
ans = beautySum(s)
print(ans)