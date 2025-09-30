## Longest Common Prefix
def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    
    if strs[0][0] != strs[1][0]:
        return ""
    
    ref = strs[0]
    strs = strs[1:len(strs)]
    for str in strs:
        ans,edge = "",""
        if len(str) < len(ref):
            edge = str
        else:
            edge = ref
        for j in range(len(edge)):
            if ref[j] == str[j]:
                ans += str[j]
            else:
                break
        ref = ans

    return ans  
    
strs = ["flower","fkow"]
ans = longestCommonPrefix(strs)
print(ans)
