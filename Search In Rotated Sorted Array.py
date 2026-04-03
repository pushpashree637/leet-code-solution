nums = nums = [1]
target = 0
for i in range(len(nums)):
    if nums[i] == target:
        print(i)
        break
else:
    print(-1)
