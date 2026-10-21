class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a set(hasmap) for all seen elements
        # look fo rhte complement in the hashmap, and return those indecis if found
        seen = {}
        
        for i, num in enumerate(nums): #i is the index of num
            diff = target - num #diff is the complement

            if diff in seen:
                return [seen[diff], i]
            seen[num] = i #add the current element to the hashmap