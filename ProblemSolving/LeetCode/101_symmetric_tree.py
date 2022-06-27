# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution:
#    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#        mylist = self.traversal(root)
#        for idx, val in enumerate(mylist):
#            if val != mylist[-1-idx]:
#                return False
            
#        return True
        
#    def traversal(self, root_node) -> List[int]:
#        self.elements = []
#        self._traversal(root_node)
#        return self.elements
    
#    def _traversal(self, curr_node):
#        if curr_node is None:
#            return
#        if curr_node.left is not None:
#            self._traversal(curr_node.left)
#        self.visit(curr_node)
#        if curr_node.right is not None:
#            self._traversal(curr_node.right)
        
#    def visit(self, curr_node):
#        if curr_node is not None:
#            self.elements.append(curr_node.val)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root.left, root.right)
    
    def isSame(self, left_node, right_node):
        if left_node is None and right_node is None:
            return True
        
        elif left_node is None or right_node is None:
            return False
        
        elif left_node.val == right_node.val and self.isSame(left_node.left, right_node.right) and self.isSame(left_node.right, right_node.left):
            return True
        
        return False
