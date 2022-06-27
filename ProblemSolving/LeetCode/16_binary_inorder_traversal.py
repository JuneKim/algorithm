# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# binary traversal
# preorder   [root][left][right]
# inorder    [left][root][right]
# postorder  [left][right][root]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._traversal(root)
    
    def _traversal(self, curr_node, curr_list = []):
        if curr_node is None:
            return []
                   
        if curr_node.left is not None:
            self._traversal(curr_node.left)
        ret_list = self.visit(curr_node, curr_list)
        if curr_node.right is not None:
            self._traversal(curr_node.right)
            
        return ret_list
        
    def visit(self, curr_node, curr_list = []):
        mylist = curr_list
        if curr_node is not None:
            mylist.append(curr_node.val)
        
        return mylist
