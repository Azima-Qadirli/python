from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the result linked list
        dummy = ListNode(0)
        # Initialize current node to dummy node
        current = dummy
        # Initialize carry to 0
        carry = 0
        
        # Iterate until both linked lists or carry still has value
        while l1 or l2 or carry:
            # Extract the values of the current nodes or set to 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of values and the carry
            total = val1 + val2 + carry
            carry, val = divmod(total, 10) # divmod divides total by 10 and returns the quotient and remainder
            
            # Create a new node with the remainder as its value
            current.next = ListNode(val)
            # Move to the next node
            current = current.next
            # Move to the next nodes of l1 and l2 if they are not None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the next node after the dummy node, which is the head of the result linked list
        return dummy.next

