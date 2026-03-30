# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        output = []
        queue = collections.deque()

        if root:
            queue.append(root)

        level = 0
        while queue:
            len_queue = len(queue)
            temp_arr= []
            for _ in range(len_queue):
                curr_element = queue.popleft()

                if curr_element.left:
                    queue.append(curr_element.left)

                if curr_element.right:
                    queue.append(curr_element.right)

                temp_arr.append(curr_element.val)
            output.append(temp_arr[-1])
            level = level + 1
        return output




        