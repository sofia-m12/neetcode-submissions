class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # each level, had two different descisions/children(include nums[i] or dont)

        res = []
        
        def dfs(idx, comb, comb_sum):
            if comb_sum == target:
                res.append(comb[:]) #add a copy of the combination
                return

            if comb_sum > target or idx > (len(nums) - 1): #ignore invalid sums/no more elements to add
                return

            # add the current num[i]
            comb.append(nums[idx])
            dfs(idx, comb, comb_sum + nums[idx]) #dont increment idx because we can reuse the current element
            comb.pop()
         
            #dont add the current element
            dfs(idx + 1, comb, comb_sum)

        dfs(0, [], 0)
        return res




        