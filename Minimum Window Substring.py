s = "ADOBECODEBANC"
t = "ABC"
result = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        ok = True        
        for ch in t:
            if sub.count(ch) < t.count(ch):
                ok = False
                break
        if ok:
            if result == "" or len(sub) < len(result):
                result = sub
print(result)
