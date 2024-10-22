# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #none handeling:
        if not head or not head.next:
            return True

        slow, fast = head, head
        #step 1: get the second half.
        while fast is not None and fast.next is not None: #the while condition needs to be specific to fast to avoid index error
            slow = slow.next
            fast = fast.next.next
            # if fast:
            # print(slow.val, fast.val)

        
        #step 2: reverse the second half, using dummy node: 
        a_list = list()
        while slow:
            a_list.append(slow.val)
            slow = slow.next
        # print(reversed(a_list))
        reversed_list = reversed(a_list)
        print(reversed_list)

        #step 3: and compare it with first half:

        for each in reversed_list:
            print(each)
            
            if head and head.next:
                if head.val != each:
                    return False
                head = head.next
        # print("here")
        return True
