class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nested loop to check each element with every other one, until the right combo is foun
        #when combo found, add index of elements to the returned list

        #If nums is only 2 elements
        if(len(nums)==2):
            return [0,1] #might need to add brackets
        target_indices = [] #List to be returned

        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if(target == (nums[i]+nums[j]) and i != j):
                    target_indices.extend([i,j]) #Adds the correct indices to the returned list
                    break
                j+=1
            i+=1
        return target_indices

        