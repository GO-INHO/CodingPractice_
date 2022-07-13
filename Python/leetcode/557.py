class Solution:
    def reverseWords(self, s: str) -> str:
        def listToString(str_list):
            result = ""
            for s in str_list:
                result += s + " "
            return result.strip()
        
        array = []
        strlist = []
        array = s.split()
        for i in range(len(array)):
            strlist.append(array[i][::-1]) # [::-1] 리버스 반환 인덱스
            
        
        s = listToString(strlist)
        return s
    
        ''' 
        "Let's take LeetCode contest"
        
        array = [] -> ["Let's", "take", "LeetCode", "contest"]
        
        strlist = [] -> ["s'teL", "ekat", "edoCteeL", "tsetnoc"]
        
        result = s'teL ekat edoCteeL tsetnoc
        
        
        '''