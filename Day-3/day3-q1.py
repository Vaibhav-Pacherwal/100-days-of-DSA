## Pow(x^n) - O(logn).
def binExpo(x, n):
    ans = 1
    power = abs(n)
    while power > 0:
        if power % 2 == 1:
            ans *= x
        x *= x
        power //= 2
    
    if n > 0:
        return ans
    else:
        return 1/ans
    

ans = binExpo(2, 9)
print(ans)