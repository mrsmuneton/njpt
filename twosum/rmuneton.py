class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            if num >= target and target != 0 and target > 0:
                continue
            for addend in range(idx+1,len(nums)):
                if nums[idx] + nums[addend] == target:
                    return [idx, addend]
