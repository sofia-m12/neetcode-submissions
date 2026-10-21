class Solution:
    def isValid(self, s: str) -> bool:
        # stack ds
        # add the first half of the string to list, then start comparing the last half as you pop each off the list
        # this will fail for case: "({}[]())" 

        #alt: every open bracket we hit, we add that cloed version to the stack, to mark the order in which they need to be seen for the string to be valid
        #once we see a closed, compare to the top of the stack, if they match, pop it off, if not, string id invalid

        #early check, stirng MUSt be of even ength or else it cant be valid
        # if len(s) % 2 != 0: #O(n)
        #     return False

        stack = [] #init stack
        otc = {"(": ")", "{": "}", "[": "]" } #map open to closed
        #iterate through str
        for ch in s: # Time: O(n)
            #if open, add closed version to stack
            if ch in otc:
                stack.append(otc[ch])
                print(stack)
                continue
            #if closed, compare to stack[-1]
            if stack and ch == stack[-1]:
                stack.pop() #remove from stack, proceed
            else:
                return False # we know immediately that s is invalid
        
        if stack:
            return False
        return True

        # Time: O(n), just length and the loop, other operations are all O(1). O(n) +  O(n) = O(2n) =  O(n)
        #Space: O(n), jus tthe stack, if we get a lopsidesd, invallid string("(((((()"), well be storing pretty much up to n
