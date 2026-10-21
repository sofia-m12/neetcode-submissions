class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Implement stack with stack, compare that inputting list is equal to outputted list
        #pop() stack into a new list
        stack = list(filter(lambda x:x.isalnum(), s.lower()))
        cstack = stack[::-1]
        return stack == cstack