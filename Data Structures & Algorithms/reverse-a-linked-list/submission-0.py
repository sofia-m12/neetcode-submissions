# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, previous = head, None
        
        #iterate while current is not null
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # After the loop, previous will be the last element of the original list,
        # also the new head of the reversed list
        return previous


        