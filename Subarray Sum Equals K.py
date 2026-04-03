nums = [1,2,3]
k = 3
count = 0
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total += nums[j]
        if total == k:
            count += 1
print(count)

