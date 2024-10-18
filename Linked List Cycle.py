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

        # read_head(head):
        # slow = ListNode(3)
        # fast = ListNode(3)

        # if slow.val == fast.val:
        #     print("matching")
        # exit()
        print("tail", head.next)

        if not head.next:
            print("false")
        
            return False

        exit()
        print(slow.val, fast.val)
        while fast.val != slow.val and slow.next:
            slow = slow.next
            fast = fast.next.next
            print(slow.val, fast.val)
            # exit()
