## String Compression
chars = ["a"]

if not chars:
    print(0)
else:
    currChar,currCharIdx,count = chars[0],0,1
    for i in range(1,len(chars)+1):
        if i == len(chars):
            chars[currCharIdx] = chars[i-1]
            currCharIdx += 1
            if count > 1:
                for j in range(len(str(count))):
                    chars[currCharIdx] = str(count)[j]
                    currCharIdx += 1
            break
        if chars[i] == currChar:
            count += 1
        else:
            chars[currCharIdx] = chars[i-1]
            currCharIdx += 1
            if count > 1:
                for j in range(len(str(count))):
                    chars[currCharIdx] = str(count)[j]
                    currCharIdx += 1
            currChar = chars[i]
            count = 1

    print(chars)
    print(currCharIdx)