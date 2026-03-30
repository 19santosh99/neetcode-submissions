# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self,root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        # first find the key node
        if key > root.val:
            # right side of the tree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # left side of the tree
            root.left = self.deleteNode(root.left, key)
        else:
            # found the node to delete
            # node has 0 children
            if root.left == None and root.right == None:
                #find a way to delete
                root = None
                return root
            elif not root.left:
                # move the tree up
                return root.right
            elif not root.right:
                #move the right tree up
                return root.left
            else:
                # find the min on the right subtree and replace
                smallestRightSideNode = self.findMinNode(root.right)
                root.val = smallestRightSideNode.val
                root.right = self.deleteNode(root.right, smallestRightSideNode.val)
        return root