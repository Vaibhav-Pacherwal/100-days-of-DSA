## Isomorphic Strings
def isIsomorphic(s,t):
    if len(s) != len(t):
        return False
    
    track = {}
    for i in range(len(s)):
        val = track.get(s[i],0)
        if val == 0:
            mapped_vals = list(track.values())
            if t[i] in mapped_vals:
                return False
            track[s[i]] = t[i]
        else:
            if val != t[i]:
                return False

    return True

s = "badc"
t = "baba"
if isIsomorphic(s,t):
    print("true")
else:
    print("false")