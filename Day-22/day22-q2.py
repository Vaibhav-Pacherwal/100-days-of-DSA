## Remove Outermost Parentheses
def removeOuterParentheses(s):
    curr,count,ans = 0,0,""
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
            if count == 0:
                ans += s[curr+1:i]
                curr = i+1

    return ans

s = "(()())(())(()(()))"
ans = removeOuterParentheses(s)
print(ans)