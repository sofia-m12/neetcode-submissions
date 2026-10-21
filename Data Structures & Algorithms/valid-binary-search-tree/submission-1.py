# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #dfs traversal(predorder?)
        # at every node, check that the left subtree value is < parent(current node)
        # vice versa with right

        def check(root, left_bound, right_bound):
            # null/empty tree check
            if not root:
                return True # a null tree does meet the requirements

            #compare/check the values(left & right are passed as the values themselves)
            if not (left_bound < root.val < right_bound):
                return False #isnt valid

            #check the subtrees(left, right)
            return check(root.left, left_bound, root.val) and check(root.right, root.val, right_bound)


        return check(root, float('-inf'), float('inf'))
            
        