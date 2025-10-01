## Sort Characters By Frequency
def maxDepth(s):
    count,maxDep = 0,0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
            maxDep = max(count,maxDep)
        elif s[i] == ')':
            count -= 1
    
    return maxDep

s = "(1+(2*3)+((8)/4))+1"
maxDep = maxDepth(s)
print(maxDep)