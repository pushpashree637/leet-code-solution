nums = [1,1,1,2,2,3]
k = 2
freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
result = []
for i in range(k):
    max_key = max(freq, key=freq.get)
    result.append(max_key)
    del freq[max_key]
print(result)
