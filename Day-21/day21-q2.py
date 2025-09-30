## Rotate String
def rotateStr(s,goal):
    if len(s) != len(goal):
        return False
    
    search_space = s+s
    ans = search_space.find(goal)
    if ans == -1:
        return False
    
    return True


s = "abab"
goal = "baba"
if rotateStr(s,goal):
    print("true")
else:
    print("false")
