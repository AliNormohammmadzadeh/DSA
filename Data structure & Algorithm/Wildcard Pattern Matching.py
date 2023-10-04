def isMatch(word,pattern , n ,m,lookup):
    if m < 0 and n < 0:
        return True 
    elif m < 0:
            return False
    elif n < 0:
        for i in range(m+1):
            if pattern(i) != '*':
                return False
        return True
    
    if not lookup[n][m]:
        if pattern[m] == '*':
            


if __name__ == "__main__":
    word = 'xyxzzxy'
    pattern = 'x***x?'
    
    lookup = [[False for x in range(len(pattern)+1)] for y in range(len(word)+1)]
    
    if isMatch(word , pattern,len(word),len(pattern),lookup):
        print("Match")
    else:
        print("No Match")