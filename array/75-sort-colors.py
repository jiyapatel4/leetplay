class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt_i = 0
        pt_j = len(nums) - 1
        pt_k = 0
        while (pt_k <= pt_j):
            if (nums[pt_k] > 1):
                val = nums[pt_k]
                nums[pt_k] = nums[pt_j]
                nums[pt_j] = val
                pt_j = pt_j - 1
            elif (nums[pt_k] < 1):
                val = nums[pt_k]
                nums[pt_k] = nums[pt_i]
                nums[pt_i] = val
                pt_i = pt_i + 1
            else:
                pt_k = pt_k + 1
        return nums
