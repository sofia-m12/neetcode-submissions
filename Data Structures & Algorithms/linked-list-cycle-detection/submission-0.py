# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #slow and fast!
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next #move fast x2 as much as slow ptr

            #check if they meet = cycle detected and return early
            if slow == fast: 
                return True
        return False #no cycle detected throughout the list