# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter = sum of longest paths from left and right subtress

        #track max diameter
        diameter = 0

        def dfs(root): #O(V + E), visit all nodes in tree
            if not root:
                return 0

            nonlocal diameter
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right) #get the longets path

        dfs(root)
        return diameter

        #space: O(V) -> worst case this tree is skewed, so recursive stack holds uptoV(nodes) calls
            