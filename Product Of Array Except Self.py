nums = [-1,1,0,-3,3]
n = len(nums)
result = []
for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= nums[j]
    result.append(product)
print(result)
