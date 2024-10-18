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

        if head and head.next is None: # we only return False when the head.val is not None but head.next is None
            # fast = head.next.next
            # print(fast.val)
            return False
        
        slow, fast = head, head.next.next

        while fast != slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            # print(slow.val, fast.val)
            #exit()
        return fast.next is not None  # return True for cycle if fast.next is not None. Otherwise fast finishes all of its moves and no cycle
