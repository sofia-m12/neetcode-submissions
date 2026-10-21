class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset(Set) is most useful in this scenario, only accepts unique elments
        store = set()
        for x in nums:
            if x in store:
                return True
            store.add(x) #else add to the set
        return False
        