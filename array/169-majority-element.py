import unittest


class Solution():
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_map = {}
        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
            if num_map[num] > len(nums) // 2 :
                return num
    def majorityElementBoyerMoore(self, nums):
        count = 0
        candidate = nums[0]
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate


class TestMajorityElement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_size_four(self):
        nums = [2, 2, 2, 1]
        output = 2
        result = self.sol.majorityElement(nums)
        resultBM = self.sol.majorityElementBoyerMoore(nums)

        self.assertEqual(result, output)
        self.assertEqual(resultBM, output)

    def test_size_one(self):
        nums = [1]
        output = 1
        result = self.sol.majorityElement(nums)
        resultBM = self.sol.majorityElementBoyerMoore(nums)

        self.assertEqual(result, output)
        self.assertEqual(resultBM, output)


if __name__ == '__main__':
    unittest.main()
    
