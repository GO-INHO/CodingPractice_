# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
        '''
I: head ( linked list )
O: list
C: 
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

E:


ds: 
algo: 

solution:
변수 2개에 head값 받아서
하나는 2칸씩
하나는 1칸씩 이동하다가
2칸씩 가던 변수가 null이면 그 때의 하나씩 가던 변수의 헤드값 반환

N : list 길이?
time:  O(N)
space: 

        '''