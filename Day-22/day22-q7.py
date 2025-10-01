## Remove All Occurrence
def removeOccurrences(s, part):
    if s.find(part) == -1:
        return s
    idx = s.find(part)
    s = s[:idx]+s[idx+len(part):len(s)]

    return removeOccurrences(s,part)

s = "daabcbaabcbc"
part = "abc"
ans = removeOccurrences(s,part)
print(ans)
