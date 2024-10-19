class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize two pointers (tortoise and hare)
        slow, fast = nums[0], nums[0]
        
        # Phase 1: Detect the cycle
        while True:
            print(slow, fast)
            slow = nums[slow]      # Move slow pointer by one step
            fast = nums[nums[fast]] # Move fast pointer by two steps
            if slow == fast:        # Cycle detected
                break
        
#         # Phase 2: Find the entrance to the cycle (duplicate number)
#         slow = nums[0]              # Reset slow pointer to the start
#         while slow != fast:          # Move both pointers one step at a time
#             slow = nums[slow]
#             fast = nums[fast]
        
#         return slow  # Slow and fast meet at the duplicate number

