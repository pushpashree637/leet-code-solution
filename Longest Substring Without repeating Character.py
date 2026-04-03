s = "pwwkew"
max_length = 0
for i in range(len(s)):
    seen = ""
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen += s[j]
    if len(seen) > max_length:
        max_length = len(seen)
print(max_length)

