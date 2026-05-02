class Solution():
    def rev(self, nums):
        k = k % len(nums)
        if k == 0:
            return nums
        full_rev = self.rev(0, len(nums) - 1, nums)
        k_rev = self.rev(0, k - 1, full_rev)
        leftover_rev = self.rev(k, len(nums) - 1, k_rev)
        return leftover_rev
    def rev(self, i, j, nums):
        while(i < j):
            swap = nums[i]
            nums[i] = nums[j]
            nums[j] = swap
            i = i + 1
            j = j - 1
        return nums 

