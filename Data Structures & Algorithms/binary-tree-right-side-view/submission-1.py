from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        #some tree traversal

        #return a list of all of the rightmost nodes at each level of the tree

            #alt: add each level to the q, add the last node in teh q to the result list!

            if root is None:
                return []

            #init q, result list
            res = []
            q = deque([root])
            # loop while q not empty
            while len(q) > 0:
                n = len(q) #number of nodes at this level
                #add the rightmost node to result list, wihtou popping
                res.append(q[n-1].val) #value!
                #for each node in q:
                for _ in range(n):
                    #pop from q
                    node = q.popleft()
                    #add children to q if not null
                    for c in [node.left, node.right]:
                        if c is not None:
                            q.append(c)
            return res

            #time: O(n), we visit eahc node in the tree once
            #space: O(n), because the q holds one level at a time, which is n/2 nodes worst case, simplifies to O(n)!