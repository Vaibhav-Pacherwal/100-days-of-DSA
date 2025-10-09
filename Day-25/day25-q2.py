## Generate all binary strings
def binStr(n,poss_val):
    for i in range(2**n):
        ans = ""
        for val in poss_val:
            if i & val:  
                ans += '1'
            else:
                ans += '0'
        print(ans)

def generateBinString(n):
    dup = n
    poss_val = []
    while dup > 0:
        poss_val.append(2**(dup-1))
        dup -= 1
    
    binStr(n,poss_val)

generateBinString(4)

