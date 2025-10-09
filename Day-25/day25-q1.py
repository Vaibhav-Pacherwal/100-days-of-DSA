## Count Good Numbers
def solve(n,i,ans):
    if i == n:
        return ans%(10**9+7)

    if i%2 == 0:
        ans *= 5
    else:
        ans *= 4
    
    ans %= 10**9+7
    
    return solve(n,i+1,ans)

def countGoodNumbers(n):
    ans = solve(n,0,1)
    return ans

n = int(input("enter n:"))
ans = countGoodNumbers(n)
print(ans)

