class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = 1
        for x in nums:
            if x in nums[a:]: #Slicing nums each iteration, checking if a number is duplicated in the rest of the array
                return True
            a+=1
        return False;

         