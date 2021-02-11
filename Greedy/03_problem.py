# 그리디 - 숫자 카드 게임

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minvalue = min(data)
    result = max(result, minvalue)
    
print(result)

'''
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minvalue = 10001

    for a in data:
        minvalue = min(minvalue, a)

    result = max(result, minvalue)

print(result)
'''
