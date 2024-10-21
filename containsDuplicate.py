class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return 

        slow, fast = 0, 0

        for slow in range(len(nums)):

            # fast = slow + 1
            # print(slow, fast)

            while fast < len(nums):

                fast += 1
                # print("fast", fast)

                if fast > len(nums) - 1: #hard enforcement
                    break
                if nums[fast] == nums[slow] and fast != slow:
                    # print("slow, fast", slow, fast)
                    return True
            fast = slow + 1


        return False
