class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map = {0:1}
        cum_sum = 0
        count = 0
        for i in range(len(nums)):
            cum_sum = cum_sum + nums[i]
            if cum_sum - k in hash_map:
                count = count + hash_map[cum_sum - k]
            if cum_sum in hash_map:
                hash_map[cum_sum] = hash_map[cum_sum] + 1
            else:
                hash_map[cum_sum] = 1
        return count