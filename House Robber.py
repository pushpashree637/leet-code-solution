nums = [1,2,3,1]
prev = 0
curr = 0
for n in nums:
    temp = max(curr, prev + n)
    prev = curr
    curr = temp
print(curr)
