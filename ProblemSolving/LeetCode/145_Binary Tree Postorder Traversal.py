# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traversal(myroot):
            if not myroot:
                return

            traversal(myroot.left)
            traversal(myroot.right)
            output.append(myroot.val)

        traversal(root)
        return output

        #if root == None:
        #    return []

        #myresult = []
        #myresult += self.postorderTraversal(root.left)
        #myresult += self.postorderTraversal(root.right)
        #myresult.append(root.val)

        #return myresult
