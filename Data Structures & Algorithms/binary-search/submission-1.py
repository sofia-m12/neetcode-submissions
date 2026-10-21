class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # searching for target, optimized(binary search)
        # if nums or target is null, return -1
        if not nums:
            return -1

        # set variables for boundaries
        left, right = 0, len(nums) - 1
        # set up while loop: <= to account for if left and right point at the same index
        while left <= right:
            mid = (left + right) // 2 #calculate mid point of search ares
            #comparisons, update variables
            if nums[mid] == target:
                return mid #return matching index!
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # if loop finishes, return -1
        return -1
        