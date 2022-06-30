def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
    
    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.' and len(answer) > 1 :
        answer = answer[1:] 
    if answer[-1] == '.':
        answer = answer[:-1]

    if answer == '':
        answer = 'a'