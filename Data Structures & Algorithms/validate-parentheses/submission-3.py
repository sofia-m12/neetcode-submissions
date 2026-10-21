class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #empty list to track parentheses
        closeMap = {"}" : "{", ")" : "(", "]" : "["} 
        #iterate through all characters in s
        for x in s:
            if x in closeMap:
                #if is a closed parentheses, check that the stack isnt empty, and that its value matches with the top of the stack
                #remove the top of the stack
                if stack and stack[-1] == closeMap[x]:
                    stack.pop()
                else: return False
            else:
                #if its an open parentheses, add it to the stack list
                stack.append(x)
        #if the stack isn't empty at the end fo the loop, return false
        return True if not stack else False

        #Time & Space: O(n)
