# 구현 - 왕실의 나이트

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1    # ord : 아스키 코드 값 반환

steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
result = 0
for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
        result += 1

print(result)