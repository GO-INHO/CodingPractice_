class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
    
        p1 = 0
        p2 = len(nums)-1
        i = len(nums)-1
        while p1 <= p2:
            if nums[p1] * nums[p1] > nums[p2] * nums[p2] :
                result[i] = nums[p1] * nums[p1]
                p1 += 1
            else:
                result[i] = nums[p2] * nums[p2]
                p2 -= 1
            i -= 1
            
        
        return(result)
                
    ''' -4 -1 0 3 10 
        ^          ^
        p1 = 0
        p2 = len(nums)-1
        
        while p1 >= p2:
        if nums[p1]^ < p2^ -> result[-i] = p1^ , p1 ++
        else p2^ p2--
        
    '''
    