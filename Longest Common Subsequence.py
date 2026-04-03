def lcs(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0    
    if s1[i] == s2[j]:
        return 1 + lcs(s1, s2, i+1, j+1)
    else:
        return max(lcs(s1, s2, i+1, j), lcs(s1, s2, i, j+1))
text1 = "abc"
text2 = "def"
print(lcs(text1, text2, 0, 0))

