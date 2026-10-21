# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split the list in half -> find the middle element
        #fast & slow
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next #slow is now at the head of the 2nd list
        slow.next = None # disconnect the lists
        
        # reverse the 2nd list
        curr = second
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # prev now has the head of the reversed list

        l1, l2 = head, prev
        while l2:
            temp2 = l2.next #save the next node in 2nd list
            temp1 = l1.next
            l1.next = l2 # connect the prev in 1st list to the new node
            l2.next = temp1 #connect to the rest of the 1st list
            l1, l2 = temp1, temp2 #update the ptrs

