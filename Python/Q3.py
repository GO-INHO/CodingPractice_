#문자열 뒤집기

S = str(input())
num0 = 0
num1 = 0
numState = int(S[0])
if numState == 0 : num0 += 1
else: num1 += 1
for i in range(len(S)):
    if int(S[i]) == 0:
        if numState == 1: 
            num0 += 1
            numState = 0
    elif int(S[i]) == 1 : 
        if numState == 0: 
            num1 += 1
            numState = 1

print(num0, num1)
print(min(num0,num1))