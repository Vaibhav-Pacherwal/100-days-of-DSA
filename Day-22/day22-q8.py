## Permutation in String
def checkInclusion(s1,s2):
    s1_freq = {}
    for ch in s1:
        s1_freq[ch] = s1_freq.get(ch,0) + 1
    
    i,k = 0,len(s1)-1
    while k < len(s2):
        j = i
        inc_freq = {}
        while j <= k:
            inc_freq[s2[j]] =  inc_freq.get(s2[j],0) + 1
            j += 1
        
        if s1_freq == inc_freq:
            return True

        i += 1
        k += 1

    return False

s1 = "ab"
s2 = "eidboaoo"
if checkInclusion(s1,s2):
    print("true")
else:
    print("false")