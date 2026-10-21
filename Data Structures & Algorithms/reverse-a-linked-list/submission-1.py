# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # want to reverse the links throughout the list.
        # head should be the last node, last should be the head
        curr = head
        prev = None
        #while curr is not null, reverse the link with a temp var
        while curr != None:
            temp = curr.next#store curr next
            curr.next = prev #point next to prev
            prev = curr # move prev along
            curr = temp  #set curr to next node in the list
        return prev #this will be the head of the reversed ll

        