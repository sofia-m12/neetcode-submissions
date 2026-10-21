# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #null check
        if root is None:
            return []
        
        res = [] # result array to store the lists of levels

        #helpfer to perform bfs traversal of the tree
        def bfs(root):
            q = deque([root])#use queue to store the nodes we need ot visit next
            while len(q) > 0:
                nums = len(q)# get number of nodes at currnet level
                level = []# initialize level
                for _ in range(nums):# go thru all nodes at current level 
                    node = q.popleft() #get current node 
                    level.append(node.val) # add to the level
                    for c in [node.left, node.right]: #  add non-null children to the q
                        if c is not None:
                            q.append(c)
                res.append(level)

        bfs(root)
        return res
                #appenf leve to the result list

        