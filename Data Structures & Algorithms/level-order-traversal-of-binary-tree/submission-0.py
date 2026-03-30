from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output_arr = []
        queue = deque()

        if not root:
            return []

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            temp_arr = []
            for _ in range(len(queue)):
                curr_element = queue.popleft()

                if curr_element.left:
                    queue.append(curr_element.left)

                if curr_element.right:
                    queue.append(curr_element.right)

                temp_arr.append(curr_element.val)
            output_arr.append(temp_arr)
            level = level + 1

        return output_arr


