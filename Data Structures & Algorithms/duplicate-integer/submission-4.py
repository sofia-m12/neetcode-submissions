class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #keep a hashmap/dict of the ints that we haveseen so far
        seen = {}
        # iterate through nums
        for n in nums:
            #checlk if current numbers is in seen, if yes -> return true
            if n in seen:
                return True
            seen[n] = 1 # add to seen
        return False

        

        