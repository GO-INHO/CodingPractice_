#프로그래머스 실패율
def solution(N, stages):
    answer = []
    dic = {}
    user_num = len(stages)
    for i in range(1, N+1):
        if user_num <= 0:
            dic[i] = 0
            continue
            
        count = stages.count(i)
        dic[i] = count / user_num
        user_num -= count
        
            
    print(dic)
    answer = [x[0] for x in sorted(dic.items(), key=lambda x : x[1], reverse = True)]
    return answer
