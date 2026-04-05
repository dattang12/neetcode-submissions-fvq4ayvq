# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        temp_left = dummy

        for _ in range(left - 1):
            temp_left = temp_left.next

        prev, curr = None, temp_left.next
        
        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        temp_left.next.next = curr
        temp_left.next = prev

        return dummy.next
        


        


        