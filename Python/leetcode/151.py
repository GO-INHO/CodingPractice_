class Solution:
    def reverseWords(self, s: str) -> str:
        def listToString(str_list):
            result = ""
            for s in str_list:
                result += s + " "
            return result.strip()
        
        s_list = s_list.split()[::-1]
        
        for i in range(len(s_list)//2):
            temp = s_list[i]
            s_list[i] = s_list[-i-1]
            s_list[-i-1] = temp
        
        return listToString(s_list)
        
        
        
        
        
'''
I: string
O: string
C:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

E:
ds: stack
algo: 

solution: 
1. 단어 단위로 스택에 push하고 하나씩 pop 하면서 결과 문자열에 더해준다. 
2. 리스트로 공백 단위로 잘라서 각 단어 인덱스 별로 스왑해 준 뒤 문자열로 합산, 공백처리 필요함

N : string의 길이
time: O(N) 
space: O(N)
 '''