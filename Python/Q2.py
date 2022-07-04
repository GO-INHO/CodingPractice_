# 곱하기 혹은 더하기

str = str(input())
result = 0

for i in range(len(str)):
    if int(str[i]) == 0 or int(str[i]) == 1:
        result = result + int(str[i])
    else:
        if result == 0 : result = int(str[i])
        else: result = result * int(str[i])
        
print(result)
