class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #2 ptrs, sorted, so opposite directions

        #assuming all input have a solution!
        #!! 1 -idende, so we can add 1

        #set up ptrs
        left, right = 0, len(numbers) - 1
        #iterate thru numbers, while l < r
        while left < right:
            #compare sum to target
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
            #decrease if larger, increase if smaller
            #return if matching
        
        return [left + 1, right + 1]

        # Time: O(n) iterate thru numbers
        # Space: O(1)
        