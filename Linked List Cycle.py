# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # pos represent the index of the node that tail connects with next
        # if pos = -1, no cycle
        #[3,2,0,-4] pos = 1
        # return False

        # Edge case: if head is None or there's only one node
        if head is None or  head.next is None: # we only return False when the head.val is not None but head.next is None
            # fast = head.next.next
            # print(fast.val)
            return False
        
        # Initialize two pointers both to head
        slow, fast = head, head
        
        # Loop until the fast pointer reaches the end of the list or pointers meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If we exit the loop, there is no cycle
        return False
