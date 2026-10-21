class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use hashmap = num : index
        # calculate and search for the complement in previous nums(the hashmap)
        seen = {} 
        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]
            seen[num] = i