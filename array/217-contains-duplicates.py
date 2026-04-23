class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
                if hash_map[num] > 1:
                    return True
            else:
                hash_map[num] = 1
        return False
