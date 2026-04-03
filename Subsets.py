nums = [1,2,3]
result = [[]]
for n in nums:
    new = []
    for sub in result:
        new.append(sub + [n])
    result += new
print(result)

