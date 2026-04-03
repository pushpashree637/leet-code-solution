coins = [2]
amount = 3
dp = [amount + 1] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)
if dp[amount] == amount + 1:
    print(-1)
else:
    print(dp[amount])
