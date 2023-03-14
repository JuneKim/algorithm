# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## runtime: 90.94%, memory: 84.4%
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def calDepthOfParent(currDepth, node, target: int):
            if node == None:
                return None, None

            if node.val != target:
                if node.left != None and node.left.val == target:
                    return currDepth + 1, node
                elif node.right != None and node.right.val == target:
                    return currDepth + 1, node
            else:
                return currDepth, None
            
            myDepth, myParent = calDepthOfParent(currDepth+1, node.left, target)
            if myDepth == None or myParent == None:
                myDepth, myParent = calDepthOfParent(currDepth+1, node.right, target)

            return myDepth, myParent


        xDepth, xParent = calDepthOfParent(0, root, x)
        yDepth, yParent = calDepthOfParent(0, root, y)

        ## different Parent
        #print (xDepth)
        #print (yDepth)
        return xDepth == yDepth and xParent != yParent
