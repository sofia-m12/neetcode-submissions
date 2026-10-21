class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force: go thru left to rught get the alphahum charctes, then go thru string backwards, and compare, but thats mroe than one pass

        #cheat: compare s to its reverse using a slice[::-1]

        #alt: 2 ptrs, opposite directions, compsrchars until they meet, or return false early
        # set up ptrs
        # iterater thru s
            #if char is not slpha num, skip until it is.
            #comapre pointers, return false if not the same (.lower() case insentitive)
            #update pointer to avoid infinite loop
        

        #return true if all chars are checked

        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1 
        return True

        