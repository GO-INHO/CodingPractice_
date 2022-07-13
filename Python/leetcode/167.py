class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        last = len(numbers)-1
        while p1 < len(numbers):
            if numbers[p1] + numbers[p2] == target and p1 != p2:
                return [p1+1, p2+1]
            
            if numbers[p1] + numbers[p2] < target and p1 != p2 :
                if p2 != last:
                    p2 += 1
                    if numbers[p1] == numbers[p2]:
                        p1 = p2-1
                else:
                    p1 += 1
            if numbers[p1] + numbers[p2] > target and p1 != p2:
                p1 += 1
                p2 = p1 + 1
                
    '''
    200
    [3,24,50,79,88,150,345]
          ^
              ^              
    I : int 배열, 오름차순
    O : 두쌍의 +1 인덱스
    C :
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.(무조건 답 존재.)
    E :
    
    
    ds: ex) 스택, 큐, 해시맵
    
    algo: 투 포인터
    
    solution:sudo code or 한국어 정리
    
    time:
    space:
    '''