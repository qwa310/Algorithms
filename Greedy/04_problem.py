# 그리디 - 1이 될 때까지

n, k = map(int, input().split())
count = 0

while n >= k:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
        
while n > 1:
    n -= 1
    count += 1

print(count)


'''
n, k = map(int, input().split())
count = 0

while n > 1:
    target = (n // k) * k 
    count += n - target     # n나누기k 했을 때의 나머지를 -1씩 해서 소거 => 나머지만큼 count함
    n = target              # n이 k로 나누어 떨어지게 만든 target 값을 n에 넣음
    if n < k:
        count += (n - 1)
        n = 1
    count += 1              # n을 k로 나눌 때의 count
    n //= k

print(count)
'''

'''
n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k 
    count += n - target     # n나누기k 했을 때의 나머지를 -1씩 해서 소거 => 나머지만큼 count함
    n = target              # n이 k로 나누어 떨어지게 만든 target 값을 n에 넣음
    if n < k:
        break
    count += 1              # n을 k로 나눌 때의 count
    n //= k

count += (n - 1)
print(count)
'''
