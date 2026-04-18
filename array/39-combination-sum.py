import unittest


class Solution():
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.recursive_combo_sum(candidates, target, 0, [], [])

    def recursive_combo_sum(self, candidates, target, start, curr_combo, result):
        if sum(curr_combo) == target:
            result.append(list(curr_combo))
            return
        elif sum(curr_combo) > target:
            return
        for i in range(start, len(candidates)):
            curr_combo.append(candidates[i])
            self.recursive_combo_sum(candidates, target, i, curr_combo, result)
            curr_combo.pop()
        return result


class TestCombinationSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_candidates_length_three(self):
        candidates = [2, 3, 6, 7]
        target = 7
        output = [[2, 2, 3], [7]]
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, output)

    def test_empty_candidates(self):
        candidates = []
        target = 3
        output = []
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, output)

    def test_single_combo(self):
        candidates = [2, 92, 28, 1, 4]
        target = 1
        output = [[1]]
        result = self.sol.combinationSum(candidates, target)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
