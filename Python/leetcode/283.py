class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #def swap(nums: List[int], p1 , p2):
        
        if len(nums) == 1: return None
        p1 = 0
        p2 = 0
        while p1 < len(nums):
            if nums[p1] != 0:
                p1 += 1
                if p1 == len(nums)-1:
                    return None
                continue
            else:
                p2 = p1 + 1
                while nums[p2] == 0:
                    p2 += 1
                    if p2 >= len(nums):
                        return None
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
                if p2 == len(nums)-1:
                    return None
            
            
            
            
            
            
            
            
            
        """
        Do not return anything, modify nums in-place instead.
        """
    
        