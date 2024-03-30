class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first=ListNode()
        current=first
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next  # Move l1 pointer to the next node
            else:
                current.next = l2
                l2 = l2.next  # Move l2 pointer to the next node
            current = current.next  # Move current pointer to the next node

        # Append the remaining nodes from either list
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return first.next  # Return the head of the merged list
