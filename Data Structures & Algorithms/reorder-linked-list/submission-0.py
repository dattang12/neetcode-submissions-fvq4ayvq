# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1 - find middle
        slow, fast = head, head
        while fast and fast.next: # Find middle
            slow = slow.next        # moves 1 step
            fast = fast.next.next   # moves 2 steps

        # step 2 - reverse second half
        prev,curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # step 3 - merge alternating
        first, second = head, prev
        res = ListNode(0)
        tail = res
        
        while second.next:          # second.next because second half contains the middle node
            next1 = first.next
            next2 = second.next

            tail.next = first
            first.next = second
            tail = second

            first = next1
            second = next2

        tail.next = first
        
            
                
            
            




            

