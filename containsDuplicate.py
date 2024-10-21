
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return 

        slow, fast = 0, 0

        while fast < len(nums) and slow != fast:
            
