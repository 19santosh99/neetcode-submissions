"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        oldtoNew = {}

        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]


            # created a new node
            copy_node = Node(node.val)

            # mapping between the old node and cloned node
            oldtoNew[node] = copy_node

            # once the main node is created we need to create neighbors
            for nei in node.neighbors:
                copy_node.neighbors.append(dfs(nei))

            return copy_node


        return dfs(node)
        
