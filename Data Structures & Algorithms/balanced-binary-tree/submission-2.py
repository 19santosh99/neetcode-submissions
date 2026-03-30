# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def calHeight(self, node):
        if not node:
            return 0

        heightleft = self.calHeight(node.left)
        heightRight = self.calHeight(node.right)
        return 1 + max(heightleft, heightRight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balancedLeft = self.isBalanced(root.left)
        balancedRight = self.isBalanced(root.right)

        heightLeft = self.calHeight(root.left)
        heightRight = self.calHeight(root.right)

        if abs(heightLeft - heightRight) <= 1 and balancedLeft and balancedRight:
            return True
        
        return False
        

