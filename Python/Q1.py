# 모험가 길드
# 그룹 최대 갯수
# in 2 3 1 2 2 out 2

n = int(input())

array = list(map(int, input().split()))
array.sort()

result = 0
count = 0
for i in range(n):
    count += 1
    if count >= array[i]:
        result += 1
        count = 0

print(result)