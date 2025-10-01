## Longest Palindromic Substring
def isPalindrome(s):
    start,end = 0,len(s)-1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
        
    return True

def longestPalindrome(s):
    longest,subStr = "",""
    for i in range(len(s)):
        for j in range(i,len(s)):
            subStr += s[j]
            if isPalindrome(subStr):
                if len(longest) < len(subStr):
                    longest = subStr
        subStr = ""
    
    return longest

s = "cbbd"
ans = longestPalindrome(s)
print(ans)