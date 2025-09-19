## Reverse vowels in a string
vowels = "AEIOUaeiou"

text = input("enter string:")
s = list(text)

start,end = 0,len(s)-1
while start <= end:
    if s[start] in vowels and s[end] in vowels:
        temp = s[start]
        s[start] = s[end]
        s[end] = temp
        start += 1
        end -= 1
    
    elif s[start] in vowels and s[end] not in vowels:
        end -= 1
    
    elif s[end ] in vowels and s[start] not in vowels:
        start += 1
    
    else:
        start += 1
        end -= 1

print("".join(s))