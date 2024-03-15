class Solution:
    def mergeTwoLists(self, l1,l2):
        dummy = ListNode(0)  # Initialize dummy node with a value
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # Move tail to the next node after merging

        # Append the remaining nodes from either list
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
