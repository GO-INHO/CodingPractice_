# 만들 수 없는 수

data = list(map(int,input().split()))
data.sort()

target = 1
for i in data:
    if target < i:
        break
    
    target += i
    
print(target)