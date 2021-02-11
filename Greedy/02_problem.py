# 그리디 - 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max = data[n-1]
min = data[n-2]
result = 0

count = int(m / (k + 1)) * k
count += m % (k+1)

result += max * count
result += min * (m - count)

print(result)
"""
5 8 3 
2 4 5 4 6
"""

'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max = data[n-1]
min = data[n-2]

sum = 0
while True:
    for i in range(k):
        sum += max
        m -= 1
        if(m == 0):
            break
    sum += min
    m -= 1
    if(m == 0):
        break

print(sum)'''
