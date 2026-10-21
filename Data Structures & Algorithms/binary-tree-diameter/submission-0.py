# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #diameter is max of sums of l & r heights!
        self.diameter = 0 #global var of the tree object

        def height(tree):
            if tree is None:
                return 0

            #update the diameter!
            left = height(tree.left)
            right = height(tree.right)
            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        height(root)
        return self.diameter

        # #height of a tree
        # def height(t):
        #     if t is None:
        #         return 0
        #     return 1 + max(height(t.left), height(t.right))
    
        # def get_diameter(r):
        #     if r is None:
        #         return 0
            
        #     # get current node's diameter 
        #     diameter = height(r.left) + height(r.right)

        #     #get max diamter in the tree
        #     return max(diameter, get_diameter(r.left),  get_diameter(r.right))
        # # return the max of all those sums
        # return get_diameter(root)
        