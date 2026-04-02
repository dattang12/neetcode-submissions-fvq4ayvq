class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        tail = None   

        if list1 and list2 is None:
            return list1
        
        if list2 and list1 is None:
            return list2
        
        if list1 is None and list2 is None:
            return list1

        head1 = list1
        head2 = list2

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                if new_head is None:
                    new_head = head1
                    tail = new_head   
                    head1 = head1.next
                else:
                    tail.next = head1
                    tail = tail.next
                    head1 = head1.next
            else:
                if new_head is None:
                    new_head = head2
                    tail = new_head
                    head2 = head2.next
                else:
                    tail.next = head2
                    tail = tail.next
                    head2 = head2.next

        while head1 is not None:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
        
        while head2 is not None:
            tail.next = head2
            tail = tail.next
            head2 = head2.next

        return new_head   