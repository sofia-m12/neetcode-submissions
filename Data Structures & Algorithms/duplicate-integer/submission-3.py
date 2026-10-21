class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #use hashmap to store seen var
        seen = {}
        for n in nums:
            if n in seen:
                return True
            else:
                seen[n] = 1
        return False
        