class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create list from s, filter out non alphanumeric + use lower()
        stack = list(filter(lambda x:x.isalnum(), s.lower()))
        #reversing stack
        cstack = stack[::-1]
        #checks if stack and cstack are equal, and returns the result of that
        return stack == cstack