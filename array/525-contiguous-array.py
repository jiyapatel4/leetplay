class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        max_len = 0
        sum = 0
        for i in range(len(nums)):
            curr_len = 0
            if nums[i] == 1:
                sum = sum + 1
            else:
                sum = sum - 1

            if sum not in hash_map:
                hash_map[sum] = i

            if sum == 0:
                curr_len = i + 1
            elif sum in hash_map:
                curr_len = i - hash_map[sum]

            if max_len < curr_len:
                max_len = curr_len

        return max_len
