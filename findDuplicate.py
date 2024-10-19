class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return

        for slow in range(len(nums)):

            fast = slow + 1
            # print(slow, fast)

            while fast < len(nums) and nums[fast] != nums[slow]:
                fast += 1
                # print(slow, fast)


            if fast >=  len(nums):
                continue
            
            if nums[fast] == nums[slow]:
                return nums[fast]
