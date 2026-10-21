# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #for each node in root(tree), check if subRoot matches(same tree)
        if root is None: #a null tree cannot have a subtree
            return False

        #check if inputs are same tree
        def sameTree(r1, r2):
            #null check
            if r1 is None and r2 is None:
                return True

            # equality check
            if r1 is None or r2 is None or r1.val != r2.val:
                return False
            
            return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)

        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        