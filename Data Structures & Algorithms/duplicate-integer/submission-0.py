class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = 1
        for x in nums:
            if x in nums[a:]:
                return True
            a+=1
        return False;

         