#효율적인 화폐 구성
#화폐 단위 ex) 2,3,5
#n = 화폐 갯수, m 찾는 숫자 (target)
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(array[i], n):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1 )
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
    