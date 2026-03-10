import unittest
class Solution():
    def productExceptSelf(self, nums):
        """
        Invariant: 
        :type nums: List[int]
        :rtype: List[int]
        """
        left_arr = []
        for i in range(len(nums)):
            if i == 0:
                left_arr.append(1)
            else:
                left_arr.append(nums[i - 1] * left_arr[i - 1])

        right_val = 1
        for j in range(len(nums) - 1, -1, -1):
            left_arr[j] *= right_val
            right_val *= nums[j]
        
        return left_arr
    
class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_four_positive_numbers(self):
        """
        Calculate the answer for four positive numbers:
        [2, 3, 4, 5]
        """
        nums = [2, 3, 4, 5]
        output = [60, 40, 30, 24]
        result = self.sol.productExceptSelf(nums)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()



        



        

