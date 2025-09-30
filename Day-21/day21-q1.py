## Valid Anagram
str1 = input("enter str1:")
str2 = input("enter str2:")

str1_freq = {}
for ch in str1:
    str1_freq[ch] = str1_freq.get(ch,0) + 1

str2_freq = {}
for ch in str2:
    str2_freq[ch] = str2_freq.get(ch,0) + 1

if str1_freq == str2_freq:
    print(f"{str1} and {str2} are anagram.")
else:
    print(f"{str1} and {str2} are not anagram.")