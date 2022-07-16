"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution: # level by level 은 BFS
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]': 
        if root == None or root.left == None: return root
        
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        
        return root
        
        
'''
Solution

dfs node
    
    node->left->next = node->right
    if node->next :
        node->right->next = node->next->left
    
    dfs(node.left)
    dfs(node.right)
    
    return node



'''