#그리디 - 거스름돈
coin_types = [500, 100, 50, 10]
change = 1260
count = 0

for coin in coin_types:
    count += int(change / coin)     # 나눗셈은 // 혹은 int(a/b)
    change %= coin

print(count)