class Solution:
    def hammingWeight(self, n: int) -> int:
        # n & 1 = 1
        count = 0

        #go through the array, adding to count
        # isolate kth bit with n >> k
        for k in range(32):
            count += (n >> k) & 1 #add bit & 1 
        return count

# Time: O(1), go thru 32 bitsm which is a constant
# space: O(1), only varibales, no extra ds for storage

        