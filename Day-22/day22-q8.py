## Permutation in String
def nextPermutation(strs):
    s = list(strs)
    pivot,i = -1,len(s)-1
    while i > 0:
        if s[i-1] < s[i]:
            pivot = i-1
            break
        i -= 1

    if pivot == -1:
        s.reverse()
        return s

    j = len(s)-1
    while j > 0:
        if s[j] > s[pivot]:
            temp = s[j]
            s[j] = s[pivot]
            s[pivot] = temp
            break
        j -= 1

    start,end = pivot+1,len(s)-1
    while start <= end:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1

    return "".join(s)

def checkInclusion(s1,s2):
    nextPerm = nextPermutation(s1)
    if s2.find(nextPerm) == -1:
        return checkInclusion(nextPerm,s2)
    
    return False
    

s1 = "ab"
s2 = "eidbaooo"
if checkInclusion(s1,s2):
    print("true")
else:
    print("false")