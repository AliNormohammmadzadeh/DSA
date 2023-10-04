def KMPSearch(pat,text):
    M = len(pat)
    N = len(text)
    
    lps = [0]*M
    j = 0
    
    comoputLPSArray(pat,M,lps)
    
    i = 0
    while i < N :
        if pat[j] == text[i]:
            i += 1 
            j += 1  
        if j == M : 
            print("Found pattern at index : " +str(i - j+1))
            j = lps[j-1]
        elif i < N and pat[j] != text[i]:
            if j != 0 :
                j = lps[j-1]
            else:
                i += 1 
        
        
    
    
def comoputLPSArray(pat, M, lps):
    lenn = 0
    lps[0]
    i = 1
    
    while i < M :
        if pat[i] == pat[lenn]:
            lenn += 1
            lps[i] = lenn
            i +=1
        else:
            if lenn != 0 :
                lenn = lps[lenn-1]
            else:
                lps[i] = 0 
                i += 1   
                
    print(lps)
            

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
txt1 = "ababcabcabababd"
pat1 = "ababd"
KMPSearch(pat1,txt1)