from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # visit every node in the tree, and swap its children
        #swap: must maintain pointers, so use a temp node
        #level-by-level traversal works well
        # bfs

        #empty case
        if root is None:
            return None
        # initialize q
        q = deque([root])
        # while loop len(q) > 0:
        while len(q) > 0:
            n = len(q) #n is the length of the current level
            #for every node at curr level
            for _ in range(n):
                #take it off the q
                node = q.popleft()
                # swap its children
                temp_node = node.left
                node.left = node.right
                node.right = temp_node
             # if they are not null add children to the q
                for c in [node.left, node.right]:
                    if c is not None:
                        q.append(c) 
    #return the root
        return root

        #time: O(n), we only visit each node once, so n nodes
        #space: O(1), constant space, no new data struture?
            # this could also be O(n), a large tree could have many noes on one level, filling up the q, however that would still be some number less that n (n - x).

        