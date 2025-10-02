## Sort Characters By Frequency
def frequencySort(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    
    ans = ""
    vals_set = set(freq.values())
    vals = sorted(vals_set)
    for i in range(len(vals)-1,-1,-1):
        keys = [k for k,v in freq.items() if v == vals[i]]
        for key in keys:
            count = freq[key]
            while count > 0:
                ans += key
                count -= 1
        
    return ans

s = "Aabb"
ans = frequencySort(s)
print(ans)