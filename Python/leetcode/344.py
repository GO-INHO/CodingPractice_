class Solution:
    def reverseString(self, s: List[str]) -> None:
        num = len(s)//2
        for i in range(num):
            temp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp
            
        