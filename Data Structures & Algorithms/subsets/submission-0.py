class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all possible subsets/sombinations => backtracking

        res, path = [], [] #list to hold all possible subsets, list to track path in the traversal
        n = len(nums)

        def dfs(idx):
            if idx == n:
                res.append(path[:]) # add copy of the current path to the res list
                return

            dfs(idx + 1) #continue down (left subtree, "not" choosing the number)
            path.append(nums[idx]) #add next number
            dfs(idx + 1) #continue down (right subtree)
            path.pop()  #backtrack

        dfs(0)
        return res

        