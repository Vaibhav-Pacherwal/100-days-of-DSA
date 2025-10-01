## Valid Palindrome
def isPalindrome(s):
    start,end = 0,len(s)-1
    if not s[start].isalnum():
        start += 1
    if not s[end].isalnum():
        end -= 1
        
    while start <= end:
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    
    return True

s = "race a car"
if isPalindrome(s):
    print("true")
else:
    print("false")