import unittest


class Solution():
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        curr_interval = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            last_val = curr_interval[1]
            next_interval = sorted_intervals[i]
            if last_val >= next_interval[0]:
                new_last_val = max(last_val, next_interval[1])
                curr_interval[1] = new_last_val
            else:
                result.append(curr_interval)
                curr_interval = next_interval
        result.append(curr_interval)
        return result


class TestMerge(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_intervals_length_three(self):
        intervals = [[5, 7], [1, 4], [2, 3]]
        output = [[1, 4], [5, 7]]
        result = self.sol.merge(intervals)
        self.assertEqual(result, output)

    def test_single_interval(self):
        intervals = [[1, 2]]
        output = [[1, 2]]
        result = self.sol.merge(intervals)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
