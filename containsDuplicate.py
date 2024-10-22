class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return 

        new_set = set()

        for each in nums:
            new_set.add(each)

        print(len(new_set))

        if len(new_set) != len(nums):
            return True
        else:
            return False
