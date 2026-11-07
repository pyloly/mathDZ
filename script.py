
n = 8
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        dp[j] = dp[j] + dp[j - 1]
print("8-я строка треугольника Паскаля:")
print(dp)
print("Сумма коэффициентов:", sum(dp))
print("Наибольший коэффициент:", max(dp))
