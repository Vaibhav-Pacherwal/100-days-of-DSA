## String to Integer (atoi)
def myAtoi(s):
    stbc = s.strip()

    if not stbc:
        return 0

    if (65 <= ord(stbc[0]) <= 90) or (97 <= ord(stbc[0]) <= 122):
        return 0

    sign = 1
    if stbc[0] in ['+','-']:
        if stbc[0] == '-':
            sign = -1
        stbc = stbc[1:]
        
    ans = []
    for ch in stbc:
        if (48 <= ord(ch) <= 57):
            ans.append(ch)
        else:
            break

    print(ans)
    ans = "".join(ans)
    if ans == "":
        return 0
    else:
        return int(ans)*sign

s = "   -042"
print(myAtoi(s))

