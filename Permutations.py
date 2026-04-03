nums = [1,2,3]
result = [[]]
for n in nums:
    new = []
    for perm in result:
        for i in range(len(perm)+1):
            new.append(perm[:i] + [n] + perm[i:])
    result = new
print(result)
