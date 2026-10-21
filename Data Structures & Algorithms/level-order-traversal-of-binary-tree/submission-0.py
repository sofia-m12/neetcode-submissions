# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs = level order traversal
        #null or empty checks
        if root is None:
            return []

        res = []
        q = deque([root]) #make queue
        while len(q) > 0: #while q is not empty, visit each level
            length = len(q) #nodes in the current level
            level = []
            for i in range(length): #iterate thru all nodes in the level
                node = q.popleft() #get 1st node in q
                level.append(node.val) #add the VALUES
                for c in [node.left, node.right]:# create a list of children
                    if c is None: #dont add/access children who are null
                        continue
                    q.append(c) #add children to the q for next level
            res.append(level)#append the list to res
        return res
        
        