from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #level order, im thinkng bfs O(n)
       
        res = [] # init final nested array
        # empty case, return []
        if root is None:
            return []
        #init q
        q = deque([root])
        #loop while q not empty
        while len(q) > 0:
            #init curr level list
            curr_level = []
            n = len(q) #nodes in the curr level
            #for every node at curr level:
            for _ in range(n):
                #pop off the q
                node = q.popleft()
                #add val to the level List
                curr_level.append(node.val)
                #add children to q, if not null
                for c in [node.left, node.right]:
                    if c is not None:
                        q.append(c)
            #add level list to the final res
            res.append(curr_level)
        #return the final q
        return res

        #time: O(n),again visited each node in the tree once
        #space: O(n), so the curr_level array holds around n/2 nodes at most at any given time, and it is cleared every level, so this simplfies to n
        